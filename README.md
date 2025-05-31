# GPU Media Stack

This project is a GPU-accelerated media stack designed to manage and stream your media collection efficiently. It leverages Docker containers to run various media-related services, all configured to work seamlessly together.

## Table of Contents

- [Overview](#overview)
- [Services](#services)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Volumes and Networks](#volumes-and-networks)
- [Troubleshooting](#troubleshooting)

## Overview

The GPU Media Stack includes the following services:

- **Emby**: A media server for organizing and streaming your media.
- **Plex**: Another popular media server with GPU acceleration.
- **Jellyfin**: A free and open-source media server.
- **Gluetun**: A VPN client to secure your network traffic.
- **Tautulli**: A monitoring tool for Plex.
- **Sonarr**: A TV show management tool.
- **Radarr**: A movie management tool.
- **Lidarr**: A music management tool.
- **Bazarr**: A subtitle management tool.
- **SABnzbd**: A Usenet downloader.

## Prerequisites

Before you begin, ensure you have the following:

- A Linux-based operating system.
- Docker and Docker Compose installed.
- NVIDIA GPU drivers installed and configured.
- Access to a VPN service (e.g., ProtonVPN).

## Setup

1. Clone this repository:

   ```zsh
   git clone <repository-url>
   cd gpu-media-stack
   ```

2. Create a `.env` file in the project root and define the following variables:

   ```env
   PROTONVPN_USER=<your-vpn-username>
   PROTONVPN_PASS=<your-vpn-password>
   ```

3. Start the stack:

   ```zsh
   docker-compose up -d
   ```

## Usage

- Access the services via the following URLs:
  - Emby: `http://localhost:8096`
  - Plex: `http://localhost:42400`
  - Jellyfin: `http://localhost:8097`
  - Sonarr: `http://localhost:8989`
  - Radarr: `http://localhost:7878`
  - Lidarr: `http://localhost:8686`
  - Bazarr: `http://localhost:6767`
  - SABnzbd: `http://localhost:8080`
  - Tautulli: `http://localhost:8181`

## Volumes and Networks

### Volumes

The stack uses the following external volumes to persist data:

- `media-emby-config`
- `media-plex-config`
- `media-jellyfin-config`
- `media-jellyfin-cache`
- `media-gluetun-config`
- `media-tautulli-config`
- `media-sonarr-config`
- `media-sabnzbd-config`
- `media-radarr-config`
- `media-lidarr-config`
- `media-bazarr-config`

### Networks

- `gpu-media-stack`: A custom bridge network for inter-container communication.

## Troubleshooting

- Ensure your NVIDIA drivers are up-to-date.
- Check the logs of individual containers for errors:

  ```zsh
  docker logs <container_name>
  ```

- Verify your `.env` file contains the correct VPN credentials.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.