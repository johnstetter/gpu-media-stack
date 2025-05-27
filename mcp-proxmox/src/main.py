"""
MCP Server implementation for Proxmox integration.
This module provides context about Proxmox VE infrastructure to LLMs.
"""

import os
from typing import Dict, List, Any
from fastapi import FastAPI, HTTPException, APIRouter
from dotenv import load_dotenv
from .proxmox_client import ProxmoxClient
from .schemas import VMInfo, NodeInfo, ClusterInfo

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Proxmox MCP Server",
    description="A Model Context Protocol server for Proxmox VE infrastructure"
)

# Initialize API router with MCP context prefix
router = APIRouter(prefix="/mcp/context")

# Initialize Proxmox client
proxmox_client = ProxmoxClient(
    host=os.getenv("PROXMOX_HOST"),
    user=os.getenv("PROXMOX_USER"),
    password=os.getenv("PROXMOX_PASSWORD"),
    verify_ssl=os.getenv("PROXMOX_VERIFY_SSL", "false").lower() == "true"
)

@router.get("/cluster")
async def get_cluster_info() -> Dict[str, Any]:
    """Get general information about the Proxmox cluster."""
    try:
        return proxmox_client.get_cluster_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/node/{node_name}")
async def get_node_info(node_name: str) -> Dict[str, Any]:
    """Get detailed information about a specific Proxmox node."""
    try:
        return proxmox_client.get_node_info(node_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/vm/{vmid}")
async def get_vm_info(vmid: int) -> Dict[str, Any]:
    """Get detailed information about a specific VM."""
    try:
        return proxmox_client.get_vm_info(vmid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/vms")
async def list_vms() -> List[Dict[str, Any]]:
    """Get a list of all VMs in the cluster."""
    try:
        return proxmox_client.list_vms()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Include router in the FastAPI app
app.include_router(router)
