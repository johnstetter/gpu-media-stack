
# 🧠 GPU AI Stack

[![Build Status](https://gitlab.com/stetter-mcp/gpu-ai-stack/badges/main/pipeline.svg)](https://gitlab.com/stetter-mcp/gpu-ai-stack/-/pipelines)
[![Docker Registry](https://img.shields.io/badge/registry-gitlab-blue)](https://gitlab.com/stetter-mcp)
[![GPU Enabled](https://img.shields.io/badge/GPU-NVIDIA-green)](https://docs.nvidia.com/datacenter/cloud-native/index.html)

A modular, GPU-accelerated, self-hosted AI stack for local LLMs, image generation, whisper-based transcription, translation, and LangChain-driven automations — with Proxmox integration and a fully containerized interface.

---

## 🧰 Stack Components

| Service               | Description |
|----------------------|-------------|
| 🧠 **Ollama**        | Local LLMs like LLaMA/Code Llama |
| 💬 **Open WebUI**    | Web chat interface with RAG + tool use |
| 🔍 **SearxNG**        | Privacy-focused metasearch for RAG queries |
| 🎨 **ComfyUI**        | Stable Diffusion image generation |
| 🌍 **LibreTranslate** | GPU-accelerated language translation |
| 🎙️ **Whishper**      | Audio transcription and translation |
| 🧮 **MongoDB**        | Database for Whisper |
| ⚡ **Redis**          | Caching for LangChain + agents |
| 🤖 **agent-proxmox** | LangChain chatbot agent backend |
| 🧰 **mcp-proxmox**   | Proxmox API integration service |

---

## 🧱 Requirements

- Docker 20.10+ and Docker Compose v2
- NVIDIA GPU with NVIDIA Container Toolkit (`nvidia-container-runtime`)
- Pre-created Docker volumes and network (see below)
- `.env` file with credentials

---

## 🗂️ Directory Structure

```
.
├── docker-compose.yml
├── .env
├── stable-diffusion-webui-docker/
│   └── services/
│       ├── comfy/
│       └── download/
├── agent-proxmox/
├── mcp-proxmox/
```

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://gitlab.com/stetter-mcp/gpu-ai-stack.git
cd gpu-ai-stack
```

2. **Create a `.env` file**

Example:

```ini
PUID=1000
PGID=1000
REDIS_PASSWORD=secretpassword
DB_USER=whisper
DB_PASS=whisper
WHISHPER_HOST=http://whisper:80
LANGCHAIN_LOG_DIR=/logs
LT_LOAD_ONLY=en,fr,es
```

3. **Create required Docker volumes**

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

4. **Create external network**

```bash
docker network create gpu-ai-stack
```

5. **Launch the stack**

```bash
docker compose up -d
```

---

## 🌍 Access Services

| App                  | URL                    |
|----------------------|------------------------|
| Open WebUI           | http://localhost:8080  |
| Whisper UI           | http://localhost:8000  |
| Stable Diffusion UI  | http://localhost:7860  |
| SearxNG              | http://localhost:8081  |
| LibreTranslate       | http://localhost:5000  |
| MongoDB              | mongodb://localhost:27017 |
| Agent-Proxmox (LangChain) | http://localhost:8501 |
| MCP-Proxmox (API)    | http://localhost:8008  |

---

## 🗺 Architecture

> Render this diagram using [Mermaid Live Editor](https://mermaid.live/edit)

```mermaid
graph TD
  OLLAMA[Ollama (LLM)] --> WEBUI[Open WebUI]
  SearxNG --> WEBUI
  WEBUI --> Redis
  Redis --> Agent[agent-proxmox]
  Agent --> MCP[mcp-proxmox]
  Whisper --> Mongo
  Whisper --> LibreTranslate
  Whisper --> WEBUI
  Comfy[Stable Diffusion / ComfyUI] --> Ollama
```

---

## 🔁 CI/CD & GitLab Registry

Images for `agent-proxmox` and `mcp-proxmox` are published to:

- [`registry.gitlab.com/stetter-mcp/agent-proxmox`](https://gitlab.com/stetter-mcp/agent-proxmox/container_registry)
- [`registry.gitlab.com/stetter-mcp/mcp-proxmox`](https://gitlab.com/stetter-mcp/mcp-proxmox/container_registry)

Example GitLab `.gitlab-ci.yml` for building + pushing:

```yaml
build_agent_proxmox:
  stage: build
  script:
    - docker build -t registry.gitlab.com/stetter-mcp/agent-proxmox:main ./agent-proxmox
    - docker push registry.gitlab.com/stetter-mcp/agent-proxmox:main
```

Use [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/) for `DOCKER_AUTH_CONFIG` or manually `docker login` with a [Deploy Token](https://docs.gitlab.com/ee/user/project/deploy_tokens/).

---

## 🧼 Cleanup

To stop and clean up everything:

```bash
docker compose down
docker network rm gpu-ai-stack
docker volume rm $(docker volume ls -qf 'name=ai-')
```

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

## 👤 Maintained By

**John Stetter**  
🛠️ DevOps Architect • 🧠 AI Tinkerer • ♿ Accessibility Advocate  
[GitLab](https://gitlab.com/stetter-mcp)

---

> _“Self-hosted AI means freedom — for your models, your data, and your imagination.”_
