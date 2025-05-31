# GPU AI Stack

This repository contains a Docker Compose stack designed for GPU-accelerated AI workloads. It includes a variety of services for AI model serving, data processing, and auxiliary tools. The stack is optimized for environments with GPU resources and is intended for developers and researchers working on AI projects.

## Table of Contents

- [Overview](#overview)
- [Services](#services)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Volumes and Networks](#volumes-and-networks)
- [Contributing](#contributing)
- [License](#license)

## Overview

This stack includes the following key services:

- **Ollama**: A service for AI model serving with GPU acceleration.
- **Open-WebUI**: A web-based interface for interacting with AI models.
- **SearxNG**: A privacy-respecting metasearch engine.
- **Stable Diffusion WebUI**: A web interface for Stable Diffusion models.
- **MongoDB**: A NoSQL database for storing application data.
- **LibreTranslate**: A GPU-accelerated translation service.
- **Whisper**: A speech-to-text service optimized for GPU.
- **Redis**: An in-memory data structure store for caching and messaging.
- **Agent-Proxmox**: A LangChain agent used to interface between the LLM and the MCP server.
- **MCP-Proxmox**: A Model Context Protocol (MCP) server designed to interface with Proxmox, including client examples.

## Prerequisites

- Docker and Docker Compose installed on your system.
- A machine with GPU support and the necessary drivers installed (e.g., NVIDIA drivers and CUDA).
- Access to the GitLab container registry for pulling private images.

## Setup

1. Clone this repository:
   ```bash
   git clone https://gitlab.com/your-repo/gpu-ai-stack.git
   cd gpu-ai-stack
   ```

2. Ensure your environment variables are set correctly. Create a `.env` file in the root directory with the following variables:
   ```env
   PUID=1000
   PGID=1000
   REDIS_PASSWORD=your_redis_password
   DB_USER=your_db_user
   DB_PASS=your_db_password
   PROXMOX_HOST=your_proxmox_host
   PROXMOX_USER=your_proxmox_user
   PROXMOX_PASSWORD=your_proxmox_password
   ```

3. Pull the required images:
   ```bash
   docker-compose pull
   ```

4. Start the stack:
   ```bash
   docker-compose up -d
   ```

## Usage

- Access the services via their respective ports:
  - Ollama: `http://localhost:11434`
  - Open-WebUI: `http://localhost:8080`
  - SearxNG: `http://localhost:8081`
  - Stable Diffusion WebUI: `http://localhost:7860`
  - MongoDB: `mongodb://localhost:27017`
  - LibreTranslate: `http://localhost:5000`
  - Whisper: `http://localhost:8000`
  - Redis: `redis://localhost:16379`
  - Agent-Proxmox: `http://localhost:8501`
  - MCP-Proxmox: `http://localhost:8008`

- Logs and data are stored in the respective volumes defined in the `docker-compose.yml` file.

## Volumes and Networks

### Volumes

The stack uses the following external volumes:

- `ai-ollama`
- `ai-open-webui`
- `ai-searxng`
- `ai-stable-diffusion-data`
- `ai-stable-diffusion-output`
- `ai-mongo-db`
- `ai-mongo-configdb`
- `ai-mongo-logs`
- `ai-libretranslate-data`
- `ai-libretranslate-cache`
- `ai-whisper-uploads`
- `ai-whisper-logs`
- `ai-whisper-models`
- `ai-redis-data`
- `ai-agent-proxmox-logs`
- `ai-mcp-proxmox`

### Networks

The stack uses the following networks:

- `gpu-ai-stack` (external)
- `default`

## Contributing

Contributions are welcome! Please open an issue or submit a merge request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
