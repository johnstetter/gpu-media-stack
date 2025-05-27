"""
ProxmoxClient class for interacting with the Proxmox API.
"""

from typing import Dict, List, Any
from proxmoxer import ProxmoxAPI

class ProxmoxClient:
    """Client for interacting with Proxmox VE API."""
    
    def __init__(self, host: str, user: str, password: str, verify_ssl: bool = False):
        """Initialize Proxmox client with connection details."""
        self.proxmox = ProxmoxAPI(
            host,
            user=user,
            password=password,
            verify_ssl=verify_ssl
        )

    def get_cluster_info(self) -> Dict[str, Any]:
        """Retrieve cluster information."""
        cluster_status = self.proxmox.cluster.status.get()
        resources = self.proxmox.cluster.resources.get()
        
        return {
            "status": cluster_status,
            "resources": resources
        }

    def get_node_info(self, node_name: str) -> Dict[str, Any]:
        """Get detailed information about a specific node."""
        node_status = self.proxmox.nodes(node_name).status.get()
        node_tasks = self.proxmox.nodes(node_name).tasks.get()
        
        return {
            "status": node_status,
            "tasks": node_tasks,
            "resources": self.proxmox.nodes(node_name).get()
        }

    def get_vm_info(self, vmid: int) -> Dict[str, Any]:
        """Get detailed information about a specific VM."""
        # Find the node hosting this VM
        for node in self.proxmox.nodes.get():
            try:
                vm_info = self.proxmox.nodes(node['node']).qemu(vmid).status.current.get()
                vm_config = self.proxmox.nodes(node['node']).qemu(vmid).config.get()
                return {
                    "status": vm_info,
                    "config": vm_config,
                    "node": node['node']
                }
            except:
                continue
        raise ValueError(f"VM with ID {vmid} not found")

    def list_vms(self) -> List[Dict[str, Any]]:
        """Get a list of all VMs in the cluster."""
        vms = []
        for node in self.proxmox.nodes.get():
            node_vms = self.proxmox.nodes(node['node']).qemu.get()
            for vm in node_vms:
                vm['node'] = node['node']
                vms.append(vm)
        return vms
