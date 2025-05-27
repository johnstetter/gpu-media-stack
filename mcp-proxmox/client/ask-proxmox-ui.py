import requests

OLLAMA_URL = "http://192.168.1.10:11434/api/generate"
MCP_BASE   = "http://192.168.1.10:8008/mcp/context"

def proxmox_qa(question: str, max_tokens: int = 256) -> str:
    try:
        # 1) Fetch cluster info and VM list
        cluster_resp = requests.get(f"{MCP_BASE}/cluster", timeout=5)
        vms_resp = requests.get(f"{MCP_BASE}/vms", timeout=5)
        cluster_resp.raise_for_status()
        vms_resp.raise_for_status()
        cluster_info = cluster_resp.json()
        vm_list = vms_resp.json()
    except Exception as e:
        return f"❌ MCP fetch failed: {e}"

    # 2) Build prompt with more relevant context
    prompt = (
        "You are an assistant that answers questions about a Proxmox Virtual Environment.\n"
        "You have access to real-time system data.\n\n"
        f"Cluster Info:\n{cluster_info}\n\n"
        f"VM List:\n{vm_list}\n\n"
        f"User Question:\n{question}\n\n"
        "Answer clearly and accurately using the above information."
    )

    # 3) Query Ollama
    payload = {
        "model":      "mistral:7b-instruct-v0.3-q4_K_M",
        "prompt":     prompt,
        "max_tokens": max_tokens,
        "temperature": 0.2,
        "stream": False
    }

    try:
        llm_resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
        llm_resp.raise_for_status()
        return llm_resp.json()["response"].strip()
    except Exception as e:
        return f"❌ Ollama error: {e}"

if __name__ == "__main__":
    question = "How many VMs are currently running?"
    answer = proxmox_qa(question)
    print("💬 LLM says:", answer)
