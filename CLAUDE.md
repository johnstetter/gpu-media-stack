# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a GPU AI Stack - a Docker Compose-based infrastructure for running GPU-accelerated AI services. The stack includes multiple AI services including Ollama (LLM serving), Open-WebUI (web interface), Stable Diffusion, Whisper (speech-to-text), LibreTranslate, and supporting services like MongoDB and Redis.

## Common Commands

### Start/Stop the Stack
- Start all services: `docker-compose up -d`
- Stop all services: `docker-compose down`
- View logs: `docker-compose logs -f [service_name]`
- Pull latest images: `docker-compose pull`

### Build Custom Images
- Build all custom images: `docker-compose build`
- Build specific service: `docker-compose build stable-diffusion-webui`
- Rebuild without cache: `docker-compose build --no-cache`

### Environment Setup
- Copy environment template: `cp .env.example .env`
- Edit environment variables in `.env` file before starting services

### Volume Management
Create required external volumes before first run:
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

### Network Setup
Create external network: `docker network create gpu-ai-stack`

## Architecture

### Service Dependencies
- **ollama**: Core LLM service (port 11434)
- **open-webui**: Web interface for LLMs, depends on ollama (port 8888)
- **searxng**: Privacy-focused search engine (port 8081)
- **stable-diffusion-webui**: ComfyUI for image generation (port 7860)
- **mongo**: Database for whisper service (port 27017)
- **translate**: LibreTranslate service for whisper (port 5000)
- **whisper**: Speech-to-text service, depends on mongo + translate (port 8000)
- **ai-redis**: Cache/messaging for agent services (port 16379)
- **agent-proxmox**: LangChain agent, depends on ai-redis (port 8501)
- **mcp-proxmox**: Model Context Protocol server (port 8008)

### Custom Built Services
Two services are built from local Dockerfiles:
- `stable-diffusion-download`: Downloads models (./stable-diffusion-webui-docker/services/download/)
- `stable-diffusion-webui`: ComfyUI interface (./stable-diffusion-webui-docker/services/comfy/)

### Environment Variables
Required variables in `.env`:
- `PUID/PGID`: User/group IDs for file permissions
- `DB_USER/DB_PASS`: MongoDB credentials
- `REDIS_PASSWORD`: Redis authentication
- `PROXMOX_HOST/USER/PASSWORD`: Proxmox connection details
- `WHISHPER_HOST`: Whisper service URL

### GPU Requirements
Services requiring GPU access:
- ollama, open-webui, stable-diffusion-webui, translate, whisper

## Helper Scripts

### Chat History Export
Use `helper-scripts/print_chat_history.py` to view Redis chat data:
```bash
cd helper-scripts
python print_chat_history.py --session-id default --host localhost --port 16379
```

### GitLab Issue Creation
`helper-scripts/create_gitlab_issues.py` creates predefined issues for project development roadmap.

## Development Notes

### Port Mappings
- Open-WebUI: 8888 (not standard 8080)
- Redis: 16379 (not standard 6379)
- All other services use standard ports

### Timezone Synchronization
All containers mount `/etc/localtime` and `/etc/timezone` for consistent time zones.

### Registry Access
Some images are pulled from GitLab container registry (`registry.gitlab.com/stetter-mcp/`). Ensure proper authentication if rebuilding.