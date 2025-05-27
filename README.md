# 🧠 GPU-AI-Stack: Local AI Chat, Generation, and Proxmox Control Suite

Welcome to the **GPU-AI-Stack**, an integrated containerized AI system that combines local LLMs, multimodal generation, and infrastructure control for your homelab or research environment. This stack stitches together:

- **LangChain-powered Proxmox agent (`agent-proxmox`)**
- **MCP control server (`mcp-proxmox`)**
- Local **LLM inference** via [Ollama](https://ollama.com)
- Multimodal generation with **Stable Diffusion Web UI**
- Search-enhanced LLM interaction via **Open WebUI** and **SearxNG**
- Full translation and transcription support using **LibreTranslate** and **Whisper**
- Fast storage and caching via **Redis** and **MongoDB**

---

## 🗺️ Architecture

```
                   ┌───────────────┐
                   │  Open WebUI   │
                   └─────┬─────────┘
                         │
             ┌───────────▼────────────┐
             │       Ollama           │
             └──────────┬─────────────┘
                        │
                        ▼
    ┌────────────┐   ┌───────────────┐   ┌────────────┐
    │ Whisper     │<->│LibreTranslate│<->│   MongoDB   │
    └────────────┘   └───────────────┘   └────────────┘

    ┌────────────┐
    │ SearxNG    │ <- used for web RAG
    └────────────┘

    ┌──────────────────────────┐
    │ Stable Diffusion Web UI  │
    └──────────────────────────┘

    ┌────────────┐   ┌────────────┐
    │agent-proxmox│<->│ ai-redis  │
    └────────────┘   └────────────┘

          ▲
          │
    ┌────────────┐
    │ mcp-proxmox│ (Proxmox controller)
    └────────────┘
```

---

## 🛠️ Setup

### Prerequisites

- Docker + Docker Compose V2
- GPU with NVIDIA drivers and `nvidia-container-toolkit`
- External volumes created (see below)

### 1. Clone

```bash
git clone https://gitlab.com/stetter-homelab/gpu-ai-stack.git
cd gpu-ai-stasck
```

### 2. Create `.env`

Copy the provided `.env.example` and customize it:

```bash
cp .env.example .env
```

Here’s what’s inside:

```env
# AI Stack (gpu-ai-stack)
OLLAMA_API_CREDENTIALS=
DB_USER=
DB_PASS=
WHISHPER_HOST=https://whisper.local
WHISPER_HOST=https://whisper.local
WHISPER_MODELS=tiny,small
PUID=1000
PGID=1000

# Proxmox Agent (agent-proxmox)
LANGCHAIN_LOG_DIR=/logs/langchain
REDIS_HOST=
REDIS_PORT=
REDIS_PASSWORD=
SESSION_ID=default

# Proxmox MCP Server (mcp-proxmox)
PROXMOX_HOST=
PROXMOX_USER=
PROXMOX_PASSWORD=
PROXMOX_VERIFY_SSL=false
```

### 3. Create Volumes (if not already)

```bash
docker volume create ai-agent-proxmox-logs
docker volume create ai-mcp-proxmox
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
```

### 4. Start Stack

```bash
docker compose up -d
```

---

## 🔍 Usage Tips (WIP!)

- Access chat UI at: [http://localhost:8080](http://localhost:8080)
- Submit Proxmox control prompts like:

  ```
  /proxmox list VMs
  /proxmox start VM 101
  /proxmox snapshot VM 102
  ```

- Access Whisper (transcription): [http://localhost:8000](http://localhost:8000)
- Access ComfyUI: [http://localhost:7860](http://localhost:7860)

---

## 📜 License

MIT. Use at your own risk.

---

## 👤 Author

Built and maintained by **John Stetter** ([@stetter](https://gitlab.com/stetter-homelab)), an accessibility-focused DevOps architect and AI tinkerer.
