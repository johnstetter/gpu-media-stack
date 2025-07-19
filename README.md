# GPU AI Stack

Docker Compose stack for GPU-accelerated AI services including LLM serving, image generation, speech processing, and infrastructure automation.

## Services

| Service | Image | Port | GPU | Description |
|---------|-------|------|-----|-------------|
| `ollama` | `ollama/ollama:0.9.5` | 11434 | ✓ | LLM inference server |
| `open-webui` | `ghcr.io/open-webui/open-webui:main` | 8888 | ✓ | Web interface for LLMs with RAG |
| `searxng` | `searxng/searxng:2025.6.26-c6e0ad9` | 8081 | - | Privacy-focused metasearch engine |
| `stable-diffusion-webui` | `comfy-ui` (local build) | 7860 | ✓ | ComfyUI for image generation |
| `stable-diffusion-download` | `comfy-download` (local build) | - | - | Model downloader (init container) |
| `mongo` | `mongo:6.0` | 27017 | - | Database for whisper service |
| `translate` | `libretranslate/libretranslate:v1.6.2-cuda` | 5000 | ✓ | GPU-accelerated translation |
| `whisper` | `pluja/web-whisper-backend:1.3.1` | 8000 | ✓ | Speech-to-text transcription |
| `ai-redis` | `redis:7-alpine` | 16379 | - | Cache and message broker |
| `agent-proxmox` | `registry.gitlab.com/stetter-mcp/agent-proxmox:main` | 8501 | - | LangChain agent for Proxmox |
| `mcp-proxmox` | `registry.gitlab.com/stetter-mcp/mcp-proxmox:main` | 8008 | - | Model Context Protocol server |

## Requirements

- NVIDIA GPU with CUDA support
- Docker with GPU runtime (`nvidia-docker2`)
- Docker Compose v2
- 16GB+ RAM recommended
- 50GB+ storage for models and data

## Quick Start

```bash
# Create external network
docker network create gpu-ai-stack

# Create external volumes
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

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start services
docker-compose up -d
```

## Configuration

### Environment Variables

Create `.env` file from `.env.example`:

```bash
# User/Group IDs for file permissions
PUID=1000
PGID=1000

# Database credentials
DB_USER=whisper
DB_PASS=your_secure_password

# Redis authentication
REDIS_PASSWORD=your_redis_password

# Whisper service configuration
WHISHPER_HOST=https://whisper.local
WHISPER_MODELS=tiny,small

# Proxmox integration
PROXMOX_HOST=your.proxmox.host
PROXMOX_USER=your_username
PROXMOX_PASSWORD=your_password
PROXMOX_VERIFY_SSL=false

# Agent configuration
LANGCHAIN_LOG_DIR=/logs/langchain
SESSION_ID=default
```

### Port Mappings

- **8888**: Open-WebUI (primary interface)
- **11434**: Ollama API
- **7860**: Stable Diffusion WebUI
- **8081**: SearxNG search
- **8000**: Whisper transcription
- **5000**: LibreTranslate API
- **8501**: Proxmox agent
- **8008**: MCP server
- **27017**: MongoDB
- **16379**: Redis

## Service Dependencies

```
ollama (base LLM service)
├── open-webui (web interface)
│   └── searxng (web search)
└── agent-proxmox
    └── ai-redis

mongo
├── translate (LibreTranslate)
└── whisper (speech-to-text)

stable-diffusion-download → stable-diffusion-webui
```

## Development

### Building Custom Images

```bash
# Build all local images
docker-compose build

# Build specific service
docker-compose build stable-diffusion-webui

# Force rebuild without cache
docker-compose build --no-cache
```

### Logs and Debugging

```bash
# View all logs
docker-compose logs -f

# Service-specific logs
docker-compose logs -f ollama
docker-compose logs -f open-webui

# Container inspection
docker-compose ps
docker-compose top
```

### Helper Scripts

```bash
# View Redis chat history
cd helper-scripts
python print_chat_history.py --session-id default

# Create GitLab issues for development roadmap
python create_gitlab_issues.py
```

## Data Persistence

All data is stored in named Docker volumes with external lifecycle management:

- **Models**: `ai-ollama`, `ai-whisper-models`, `ai-stable-diffusion-data`
- **User Data**: `ai-open-webui`, `ai-mongo-db`
- **Cache**: `ai-libretranslate-cache`, `ai-redis-data`
- **Logs**: `ai-whisper-logs`, `ai-mongo-logs`, `ai-agent-proxmox-logs`

## Network Architecture

- **gpu-ai-stack**: External network for service communication
- **default**: Bridge network for internal container communication

Services communicate via container names on the shared network.
