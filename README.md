# Docker Compose Container Stacks
=======
# compose-stacks

This repository contains various Docker Compose stacks organized by function:

## Stacks Overview

### AI Stack (`ai-stack`)

- **Ollama:** Local LLM inference engine supporting GPU acceleration.
- **Open WebUI:** Web interface for chat interfaces and model interactions, integrated with Ollama.
- **SearXNG:** Privacy-focused metasearch engine for web searches used in retrieval-augmented generation (RAG).
- **Stable Diffusion (ComfyUI):** Local web-based interface for image generation.
- **MongoDB:** NoSQL database supporting Whisper.
- **Whisper:** GPU-accelerated transcription service with LibreTranslate integration for multilingual translations.

### Media Stack (`media-stack`)

- **Emby:** Media server providing video streaming with GPU transcoding support.
- **Plex:** Popular media server with GPU-accelerated transcoding.
- **Jellyfin:** Open-source media server with hardware transcoding capabilities.

### WordPress Stack (`wordpress-stack`)

- **WordPress:** Popular blogging and content management platform.
- **MySQL:** Relational database backend.
- **phpMyAdmin:** Web-based administration tool for MySQL.

### TubeArchivist Stack (`tubearchivist-stack`)

- **TubeArchivist:** Video archiving and YouTube indexing tool.
- **ElasticSearch:** Search and analytics engine for indexing TubeArchivist data.
- **Redis:** High-performance key-value store used by TubeArchivist.

### Infrastructure Stack (`infra-stack`)

- **Portainer Agent:** Remote agent for managing Docker environments through Portainer UI.

---

## Usage Instructions

### Start a Stack

Navigate to the desired stack directory and start containers in detached mode:
```shell
docker compose up -d
```

**Example:**
```shell
cd ai-stack
docker compose up -d
```
---

### Stop a Stack

Navigate to the stack directory and stop/remove containers:
```shell
docker compose down
```

**Example:**
```shell
cd ai-stack
docker compose down
```

---

### Update or Rebuild Containers

Pull the latest images and recreate containers with:
```shell
docker compose pull
docker compose up -d –build
```

**Example:**
```shell
cd ai-stack
docker compose pull
docker compose up -d –build
```

---

---

### Check Container Logs

To stream container logs in real-time, run:
```shell
docker compose logs -f
```

**Example:**
```shell
cd ai-stack
docker compose logs -f
```

---

## Environment Variables and Secrets

Sensitive credentials and configuration parameters are stored in `.env` files located at the root of each stack directory. These files are intentionally excluded from version control.

### Recommended `.gitignore`

Include the following `.gitignore` at the repository root to avoid leaking sensitive data:
```
.env
*.log
.DS_Store
```

---

## Initial Setup and Database Initialization

- **WordPress Stack:** On first run, WordPress automatically initializes the database based on environment variables.
- **TubeArchivist Stack:** On first run, TubeArchivist initializes its Elasticsearch indices automatically.

---

## Accessing Services

Here are default ports for primary service access:

### AI Stack
| Service                 | URL                            |
|-------------------------|--------------------------------|
| Open WebUI              | `http://localhost:8080`        |
| Ollama API              | `http://localhost:11434`       |
| SearXNG                 | `http://localhost:8081`        |
| Stable Diffusion (UI)   | `http://localhost:7860`        |
| Whisper API             | `http://localhost:8000`        |



# Docker Compose Container Stacks

This repository contains various Docker Compose stacks organized by function:

## Stacks Overview

### AI Stack (`ai-stack`)

- **Ollama:** Local LLM inference engine supporting GPU acceleration.
- **Open WebUI:** Web interface for chat interfaces and model interactions, integrated with Ollama.
- **SearXNG:** Privacy-focused metasearch engine for web searches used in retrieval-augmented generation (RAG).
- **Stable Diffusion (ComfyUI):** Local web-based interface for image generation.
- **MongoDB:** NoSQL database supporting Whisper.
- **Whisper:** GPU-accelerated transcription service with LibreTranslate integration for multilingual translations.

### Media Stack (`media-stack`)

- **Emby:** Media server providing video streaming with GPU transcoding support.
- **Plex:** Popular media server with GPU-accelerated transcoding.
- **Jellyfin:** Open-source media server with hardware transcoding capabilities.

### WordPress Stack (`wordpress-stack`)

- **WordPress:** Popular blogging and content management platform.
- **MySQL:** Relational database backend.
- **phpMyAdmin:** Web-based administration tool for MySQL.

### TubeArchivist Stack (`tubearchivist-stack`)

- **TubeArchivist:** Video archiving and YouTube indexing tool.
- **ElasticSearch:** Search and analytics engine for indexing TubeArchivist data.
- **Redis:** High-performance key-value store used by TubeArchivist.

### Infrastructure Stack (`infra-stack`)

- **Portainer Agent:** Remote agent for managing Docker environments through Portainer UI.

---

## Usage Instructions

### Start a Stack

Navigate to the desired stack directory and start containers in detached mode:
```shell
docker compose up -d
```

**Example:**
```shell
cd ai-stack
docker compose up -d
```
---

### Stop a Stack

Navigate to the stack directory and stop/remove containers:
```shell
docker compose down
```

**Example:**
```shell
cd ai-stack
docker compose down
```

---

### Update or Rebuild Containers

Pull the latest images and recreate containers with:
```shell
docker compose pull
docker compose up -d –build
```

**Example:**
```shell
cd ai-stack
docker compose pull
docker compose up -d –build
```

---

---

### Check Container Logs

To stream container logs in real-time, run:
```shell
docker compose logs -f
```

**Example:**
```shell
cd ai-stack
docker compose logs -f
```

---

## Environment Variables and Secrets

Sensitive credentials and configuration parameters are stored in `.env` files located at the root of each stack directory. These files are intentionally excluded from version control.

### Recommended `.gitignore`

Include the following `.gitignore` at the repository root to avoid leaking sensitive data:
```
.env
*.log
.DS_Store
```

---

## Initial Setup and Database Initialization

- **WordPress Stack:** On first run, WordPress automatically initializes the database based on environment variables.
- **TubeArchivist Stack:** On first run, TubeArchivist initializes its Elasticsearch indices automatically.

---

## Accessing Services

Here are default ports for primary service access:

### AI Stack
| Service                 | URL                            |
|-------------------------|--------------------------------|
| Open WebUI              | `http://localhost:8080`        |
| Ollama API              | `http://localhost:11434`       |
| SearXNG                 | `http://localhost:8081`        |
| Stable Diffusion (UI)   | `http://localhost:7860`        |
| Whisper API             | `http://localhost:8000`        |

>>>>>>> a011806 (Initial commit: Add Docker Compose stacks)
### Media Stack
| Service                 | URL                            |
|-------------------------|--------------------------------|
| Emby                    | `http://localhost:8096`        |
| Plex                    | `http://localhost:42400`       |
| Jellyfin                | `http://localhost:8097`        |

### WordPress Stack
| Service                 | URL                            |
|-------------------------|--------------------------------|
| WordPress               | `http://localhost:8888`        |
| phpMyAdmin              | `http://localhost:3001`        |

### TubeArchivist Stack
| Service                 | URL                            |
|-------------------------|--------------------------------|
| TubeArchivist           | `http://localhost:8001`        |

### Infrastructure Stack
- Portainer Agent: Managed via external Portainer server.
| Service                 | URL                            |
|-------------------------|--------------------------------|
| Portainer Agent         | `http://localhost:9001`        |

---

## Contributing and Issues

For contributions, please create pull requests or open issues on GitLab. Ensure all sensitive data remains excluded from version control.

