import os
import logging
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import requests

from langchain.agents import Tool, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_community.llms import Ollama

# Setup logging
log_dir = os.getenv("LANGCHAIN_LOG_DIR", "./logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"langchain_{datetime.now().strftime('%Y%m%d')}.log")
logging.basicConfig(filename=log_file, filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

# Redis memory setup
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_password = os.getenv("REDIS_PASSWORD", None)
history = RedisChatMessageHistory(
    url=f"redis://:{redis_password}@{redis_host}:{redis_port}/0",
    ttl=604800,
    session_id="default"
)
memory = ConversationBufferMemory(chat_memory=history, return_messages=True)

# LLM via Ollama
llm = Ollama(model="mistral:7b-instruct-v0.3-q4_K_M", base_url="http://ollama:11434")

# Define MCP tools
def get_vms():
    resp = requests.get("http://mcp:8008/mcp/context/vms", timeout=5)
    resp.raise_for_status()
    return str(resp.json())

def get_cluster():
    resp = requests.get("http://mcp:8008/mcp/context/cluster", timeout=5)
    resp.raise_for_status()
    return str(resp.json())

tools = [
    Tool(name="get_vm_list", func=get_vms, description="Returns list of all VMs and their statuses."),
    Tool(name="get_cluster_info", func=get_cluster, description="Returns high-level Proxmox cluster status info."),
]

# Build the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    memory=memory,
    agent="conversational-react-description",
    verbose=True
)

# FastAPI app
app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    reply = agent.run(req.message)
    logging.info(f"USER: {req.message}\nAGENT: {reply}")
    return {"response": reply}
