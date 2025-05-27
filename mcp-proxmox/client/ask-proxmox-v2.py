import requests

OLLAMA_URL = "http://192.168.1.10:11434/api/generate"
MCP_BASE   = "http://192.168.1.10:8008/mcp/context"

def proxmox_qa(question: str, max_tokens: int = 256) -> str:
    try:
        # Fetch cluster and VM info
        cluster_resp = requests.get(f"{MCP_BASE}/cluster", timeout=5)
        vms_resp = requests.get(f"{MCP_BASE}/vms", timeout=5)
        cluster_resp.raise_for_status()
        vms_resp.raise_for_status()

        cluster_info = cluster_resp.json()
        vm_list = vms_resp.json()
    except Exception as e:
        return f"❌ MCP fetch failed: {e}"

    # Filter to running VMs only
    running_vms = [vm for vm in vm_list if vm.get("status") == "running"]
    vm_summary = "\n".join(f"- {vm.get('name', 'unknown')} (id: {vm.get('vmid')}, node: {vm.get('node')})"
                           for vm in running_vms)

    # Build prompt using filtered data
    prompt = (
        "You are an expert assistant for Proxmox Virtual Environments.\n"
        "Use the real-time cluster and VM data provided to answer questions accurately.\n\n"
        f"Cluster Info:\n{cluster_info}\n\n"
        f"Running VMs ({len(running_vms)}):\n{vm_summary or 'None'}\n\n"
        f"User Question: {question}\n"
        "Answer clearly and concisely."
    )

    # Query Ollama
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
    question = "How many VMs are currently running and what are their names?"
    answer = proxmox_qa(question)
    print("💬 LLM says:", answer)
