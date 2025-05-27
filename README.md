# GPU AI Stack

This project provides a self-hosted, GPU-accelerated AI stack powered by Docker Compose. It includes local LLM serving (via Ollama), multimodal AI (image generation, translation, transcription), and an extensible chat interface with tools like RAG search and Proxmox integration.

---

## 🚀 Stack Overview

| Service               | Description |
|----------------------|-------------|
| **Ollama**           | Local LLM runtime with GPU support |
| **Open WebUI**       | Chat interface for Ollama with RAG search |
| **SearxNG**          | Privacy-focused metasearch engine for RAG |
| **Stable Diffusion** | Image generation with ComfyUI backend |
| **LibreTranslate**   | GPU-enabled translation microservice |
| **Whishper**         | Audio transcription and translation UI |
| **MongoDB**          | Used by Whishper for storage |
| **Redis**            | Caching for agent-proxmox (LangChain) |
| **agent-proxmox**    | LangChain-based interface to MCP |
| **mcp-proxmox**      | Proxmox API integration backend |

---

## 🧱 Requirements

- Docker 20.10+ and Docker Compose v2
- GPU with NVIDIA Container Toolkit installed
- External Docker volumes pre-created (see below)
- `.env` file with secrets and configs

---

## 📦 Setup

1. **Clone the Repo**

```bash
git clone https://gitlab.com/stetter-mcp/gpu-ai-stack.git
cd gpu-ai-stack
```

2. **Create `.env` File**

Here's a starter template you can tweak:

```ini
# Permissions
PUID=1000
PGID=1000

# Redis
REDIS_PASSWORD=yourstrongpassword

# Whisper
WHISHPER_HOST=http://whisper:80

# Mongo
DB_USER=whisper
DB_PASS=whisper

# LangChain
LANGCHAIN_LOG_DIR=/logs

# Translate
LT_LOAD_ONLY=en,fr,es
```

3. **Create External Volumes**

```bash
docker volume create ai-ollama
docker volume create ai-open-webui
docker volume create ai-searxng
docker volume create ai-stable-diffusion-data
docker volume create ai-stable-diffusion-output
docker volume create ai-mongo-db
docker volume create ai-mongo-configdb
docker volume create ai-mongo-logs
docker volume create ai-libretranslate-data
docker volume create ai-libretranslate-cache
docker volume create ai-whisper-uploads
docker volume create ai-whisper-logs
docker volume create ai-whisper-models
docker volume create ai-redis-data
docker volume create ai-agent-proxmox-logs
docker volume create ai-mcp-proxmox
```

4. **Create the External Network**

```bash
docker network create gpu-ai-stack
```

5. **Start the Stack**

```bash
docker compose up -d
```

---

## 🌐 Accessing Services

| Service            | URL |
|-------------------|-----|
| **Open WebUI**    | [http://localhost:8080](http://localhost:8080) |
| **Stable Diffusion** | [http://localhost:7860](http://localhost:7860) |
| **Whisper UI**    | [http://localhost:8000](http://localhost:8000) |
| **SearxNG**       | [http://localhost:8081](http://localhost:8081) |
| **LibreTranslate**| [http://localhost:5000](http://localhost:5000) |
| **MongoDB**       | `mongodb://localhost:27017` |
| **Proxmox Agent UI** | [http://localhost:8501](http://localhost:8501) |
| **MCP Proxmox API** | [http://localhost:8008](http://localhost:8008) |

---

## 🧠 Agent and MCP Integration

This stack includes two GitLab-hosted services:

- **agent-proxmox**: LangChain-based interface for LLM-to-Proxmox tasks
- **mcp-proxmox**: REST API bridge to Proxmox VE nodes

You can issue LLM chat prompts (e.g., in Open WebUI) that forward Proxmox requests via these services using a custom `/proxmox` plugin or slash command handler.

---

## 🧹 Cleanup

```bash
docker compose down
docker volume prune
docker network rm gpu-ai-stack
```

---

## 🛠 Dev Notes

- GPU access is enabled via `gpus: "all"` — ensure your NVIDIA drivers + container toolkit are installed.
- Bind mounts like `/etc/timezone` and `/etc/localtime` ensure proper container time sync.
- All models and data are persisted via named external volumes.

---

## ✨ Credits

- [Ollama](https://ollama.com/)
- [Open WebUI](https://github.com/open-webui/open-webui)
- [SearxNG](https://searxng.github.io/)
- [LibreTranslate](https://libretranslate.com/)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Whishper](https://github.com/pluja/whishper)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Proxmox VE](https://www.proxmox.com/proxmox-ve)

---

## 🤖 Maintainer

**John Stetter**  
Self-hosted AI tinker • Wheelchair adventurer • GPU stack wrangler  
[GitLab](https://gitlab.com/stetter-mcp)
