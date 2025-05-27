# LangChain Agent

A lightweight FastAPI service that provides a chat endpoint backed by LangChain and Redis-based message history. This service uses an Ollama LLM for responses and persists conversations in Redis.

## Repository Structure

```bash
langchain-agent/
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md
```

- **Dockerfile**: Builds a slim Python image with the application and dependencies.
- **app.py**: FastAPI application defining a `/chat` endpoint that runs a `ConversationChain` with `ConversationBufferMemory` and Redis-backed history.
- **requirements.txt**: Python dependencies needed to run the agent.

## Prerequisites

- Docker Engine (20.x+)
- Redis instance accessible by the agent
- (Optional) Docker Compose if integrating into a larger stack

## Environment Variables

| Variable            | Default       | Description                                       |
|---------------------|---------------|---------------------------------------------------|
| `REDIS_HOST`        | `localhost`   | Hostname or IP of your Redis server               |
| `REDIS_PORT`        | `6379`        | Port number of your Redis server                  |
| `REDIS_PASSWORD`    | _none_        | Password for Redis (required if Redis is secured) |
| `LANGCHAIN_LOG_DIR` | `./logs`      | Directory path (inside container) for logs        |

Make sure to set `REDIS_PASSWORD` if your Redis instance requires authentication.

## Building the Docker Image

From within the `langchain-agent` directory:

```bash
docker build -t langchain-agent .
```

## Running the Container

A minimal `docker run` example:

```bash
docker run -d \
  --name langchain-agent \
  -p 8501:8501 \
  -e REDIS_HOST=ai-redis \
  -e REDIS_PORT=6379 \
  -e REDIS_PASSWORD=$REDIS_PASSWORD \
  -e LANGCHAIN_LOG_DIR=/logs \
  -v $(pwd)/logs:/logs \
  langchain-agent
```

This exposes the FastAPI app on port `8501` and mounts a local `logs/` directory for persistent logging.

## Integrating with Docker Compose

If you have a larger Docker Compose setup, add this service:

```yaml
services:
  langchain-agent:
    build: ./langchain-agent
    container_name: langchain-agent
    networks:
      - ai-stack
    depends_on:
      - ai-redis
    environment:
      - REDIS_HOST=ai-redis
      - REDIS_PORT=6379
      - REDIS_PASSWORD=${REDIS_PASSWORD}
      - LANGCHAIN_LOG_DIR=${LANGCHAIN_LOG_DIR}
    volumes:
      - ./langchain-agent/logs:${LANGCHAIN_LOG_DIR}
    ports:
      - "8501:8501"
```

## API Usage

Send a POST request to `/chat` with a JSON body `{ "message": "Your question here" }`:

```bash
curl -X POST http://localhost:8501/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello, LangChain!"}'
```

Response:

```json
{ "response": "<LLM reply>" }
```


## Logs

Conversation logs are written to `langchain_YYYYMMDD.log` in the `LANGCHAIN_LOG_DIR` directory. Adjust verbosity by modifying the `logging.basicConfig` settings in `app.py`.

---

Happy chaining!


