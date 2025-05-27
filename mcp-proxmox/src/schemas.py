"""
Pydantic models for request/response validation.
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class VMInfo(BaseModel):
    """VM information model."""
    vmid: int
    name: str
    status: str
    node: str
    cpu: float
    maxcpu: int
    mem: int
    maxmem: int
    disk: int
    maxdisk: int
    uptime: Optional[int]
    config: Dict[str, Any]

class NodeInfo(BaseModel):
    """Node information model."""
    node: str
    status: str
    cpu: float
    maxcpu: int
    mem: int
    maxmem: int
    disk: int
    maxdisk: int
    uptime: int
    tasks: List[Dict[str, Any]]

class ClusterInfo(BaseModel):
    """Cluster information model."""
    nodes: List[str]
    quorum: Dict[str, Any]
    resources: List[Dict[str, Any]]
