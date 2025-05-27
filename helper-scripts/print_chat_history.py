import redis
import json
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path

# Load .env from one level up (e.g. project root)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Print chat history from Redis.")
parser.add_argument("--session-id", help="Redis session ID", default=os.getenv("SESSION_ID", "default"))
parser.add_argument("--host", help="Redis host", default=os.getenv("REDIS_HOST", "localhost"))
parser.add_argument("--port", help="Redis port", type=int, default=int(os.getenv("REDIS_PORT", 6379)))
parser.add_argument("--password", help="Redis password (optional)", default=os.getenv("REDIS_PASSWORD", ""))
parser.add_argument("--output", help="Optional file to write output to (instead of stdout)", default=None)

args = parser.parse_args()

# Build Redis connection arguments
redis_args = {
    "host": args.host,
    "port": args.port,
    "decode_responses": True
}
if args.password:
    redis_args["password"] = args.password

# Connect to Redis
try:
    r = redis.StrictRedis(**redis_args)
    key = f"message_store:{args.session_id}"
    messages = r.lrange(key, 0, -1)
except redis.AuthenticationError:
    print("❌ Authentication failed. Either remove the password or configure it correctly.")
    exit(1)
except redis.RedisError as e:
    print(f"❌ Redis error: {e}")
    exit(1)

# Format output
lines = [f"Chat history for session: '{args.session_id}'", "-" * 40]
for i, msg in enumerate(messages):
    try:
        data = json.loads(msg)
        sender = data.get("type", "unknown").upper()
        content = data.get("data", {}).get("content", "")
        lines.append(f"{i+1:02d}. [{sender}] {content}")
    except json.JSONDecodeError:
        lines.append(f"{i+1:02d}. [ERROR] Could not parse message: {msg}")

output = "\n".join(lines)

# Print or write to file
if args.output:
    with open(args.output, "w") as f:
        f.write(output + "\n")
else:
    print(output)

