# Proxmox MCP Server

This is a Model Context Protocol (MCP) server that interfaces with a Proxmox VE server to provide infrastructure context to LLMs. The server exposes various endpoints that allow LLMs to query information about the Proxmox cluster, nodes, and virtual machines.

## Features

- Get cluster-wide information
- Query specific node details
- Get VM information and status
- List all VMs in the cluster
- Docker and Docker Compose support for easy deployment
- Secure credential management through environment variables

## Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- Access to a Proxmox VE server
- Proxmox API credentials

## Installation

1. Clone the repository
2. Copy `.env.example` to `.env` and update with your Proxmox credentials:
   ```bash
   cp .env.example .env
   ```
3. Update the .env file with your Proxmox credentials:
   ```
   PROXMOX_HOST=your_proxmox_host
   PROXMOX_USER=your_proxmox_user@pam
   PROXMOX_PASSWORD=your_proxmox_password
   PROXMOX_VERIFY_SSL=false
   ```

## Running with Docker Compose

1. Build and start the container:
   ```bash
   docker-compose up --build
   ```

2. The server will be available at `http://localhost:8008`

## API Endpoints

The MCP server provides the following context endpoints:

- `get_cluster_info`: Returns general information about the Proxmox cluster
- `get_node_info`: Returns detailed information about a specific Proxmox node
- `get_vm_info`: Returns detailed information about a specific VM
- `list_vms`: Returns a list of all VMs in the cluster

## Development

To run the server locally for development:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   uvicorn src.main:app --reload
   ```

## Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. Run tests and format code:
   ```bash
   pytest
   black src/ tests/
   flake8 src/ tests/
   ```
4. Commit your changes:
   ```bash
   git commit -am 'Add some feature'
   ```
5. Push to the branch:
   ```bash
   git push origin feature/my-new-feature
   ```
6. Submit a merge request

### Development Guidelines

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation when necessary
- Use type hints
- Write clear commit messages

## License

MIT
