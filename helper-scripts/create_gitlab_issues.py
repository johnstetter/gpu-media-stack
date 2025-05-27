import requests
import os
import json

GITLAB_API_URL = "https://gitlab.com/api/v4"
PROJECT_ID = os.getenv("GITLAB_PROJECT_ID", "your-namespace/your-project")
PRIVATE_TOKEN = os.getenv("GITLAB_TOKEN")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

headers = {
    "PRIVATE-TOKEN": PRIVATE_TOKEN,
    "Content-Type": "application/json"
}

issues = [
    {
        "title": "Make LLM Model Configurable via .env",
        "description": """**Description:**  
Update `app.py` to read the model name from an environment variable (`OLLAMA_MODEL`) instead of hardcoding it.

**Acceptance Criteria:**
- [ ] `app.py` reads model from `os.getenv("OLLAMA_MODEL", "llama3.2:3b")`
- [ ] `.env` includes a default model name like `OLLAMA_MODEL=llama3.2:3b`
- [ ] Docker Compose passes the `.env` value through correctly
- [ ] Changing the model in `.env` and rebuilding reflects in the agent"""
    },
    {
        "title": "Add Multi-Session / Multi-User Memory Support",
        "description": """**Description:**  
Enable multiple users/sessions by supporting a `session_id` in the API POST payload and mapping Redis keys accordingly.

**Acceptance Criteria:**
- [ ] POST body supports optional `session_id`
- [ ] Redis keys are formatted as `message_store:<session_id>`
- [ ] Defaults to `message_store:default` if `session_id` is not provided
- [ ] Memory is correctly separated between sessions"""
    },
    {
        "title": "Add /healthz Endpoint to LangChain Agent",
        "description": """**Description:**  
Expose a health check endpoint to validate Ollama and Redis availability, and show current model name.

**Acceptance Criteria:**
- [ ] `GET /healthz` returns 200 when all services are healthy
- [ ] Redis availability is verified with a ping or simple command
- [ ] Ollama model availability is verified via a metadata check
- [ ] JSON response includes: `{"redis": true, "ollama": true, "model": "llama3.2:3b"}`"""
    },
    {
        "title": "Implement Basic Tool Calling Framework",
        "description": """**Description:**  
Stub in early tool use logic for future use with Home Assistant, shell commands, or document processing.

**Acceptance Criteria:**
- [ ] Special prompt format (e.g., `!turn_off_lights`) triggers tool logic
- [ ] Tool router prints or logs what would be called
- [ ] Responses include simulated confirmation (e.g., "Simulated: Turning off lights")
- [ ] Tool handler is modular and ready for expansion"""
    },
    {
        "title": "Improve Error Handling and Logging",
        "description": """**Description:**  
Enhance error feedback in API and logging output for easier debugging and HA integration.

**Acceptance Criteria:**
- [ ] Exceptions are caught and returned as `{"error": "description"}`
- [ ] Full stack traces are written to logs
- [ ] Uncaught exceptions don’t crash the agent
- [ ] Optional: use structured JSON logging"""
    },
    {
        "title": "Add RAG / Vector Store Integration",
        "description": """**Description:**  
Allow the agent to use a local vector DB (e.g., Chroma) for document-based Q&A and richer context.

**Acceptance Criteria:**
- [ ] Chroma (or similar) container is added to Docker Compose
- [ ] A script or API to add documents to the vector store is available
- [ ] Agent retrieves top-k relevant chunks based on query
- [ ] Chat responses reference retrieved context"""
    },
    {
        "title": "Add Redis Chat History Export Script to Repo",
        "description": """**Description:**  
Add the `print_chat_history.py` script to the repo for viewing/formatting stored Redis chat data.

**Acceptance Criteria:**
- [ ] Script connects to Redis using `.env` vars
- [ ] Accepts a `--session-id` argument (defaults to `default`)
- [ ] Pretty-prints message history in readable format
- [ ] Script is added under `scripts/` or `tools/` with a brief README"""
    },
]

for issue in issues:
    if DRY_RUN:
        print(f"DRY RUN: Would create issue '{issue['title']}'")
    else:
        response = requests.post(
            f"{GITLAB_API_URL}/projects/{PROJECT_ID}/issues",
            headers=headers,
            json=issue
        )
        if response.ok:
            print(f"✅ Created: {issue['title']}")
        else:
            print(f"❌ Failed to create: {issue['title']}")
            print(response.text)
