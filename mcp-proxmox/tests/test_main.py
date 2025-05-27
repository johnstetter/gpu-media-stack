"""
Tests for the Proxmox MCP Server.
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

# Mock the ProxmoxAPI before importing app
with patch('proxmoxer.ProxmoxAPI') as MockProxmoxAPI:
    from src.main import app
    from src.proxmox_client import ProxmoxClient

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_proxmox_api():
    """Mock ProxmoxAPI for all tests."""
    with patch('proxmoxer.ProxmoxAPI') as mock:
        mock_api = Mock()
        mock.return_value = mock_api
        # Set up common mock responses
        mock_api.cluster.status.get.return_value = [{"type": "cluster"}]
        mock_api.cluster.resources.get.return_value = []
        mock_api.nodes.get.return_value = [{"node": "test-node"}]
        yield mock

def test_get_cluster_info(mock_proxmox_api):
    """Test the cluster info endpoint."""
    expected_data = {
        "status": [{"type": "cluster"}],
        "resources": []
    }
    
    response = client.get("/mcp/context/cluster")
    assert response.status_code == 200
    assert response.json() == expected_data

def test_list_vms(mock_proxmox_api):
    """Test the list VMs endpoint."""
    mock_vm = {"vmid": 100, "name": "test-vm", "status": "running"}
    mock_proxmox_api.return_value.nodes.return_value.qemu.get.return_value = [mock_vm]
    
    response = client.get("/mcp/context/vms")
    assert response.status_code == 200
    assert response.json()[0]["vmid"] == 100

def test_get_node_info(mock_proxmox_api):
    """Test getting information about a specific node."""
    mock_status = {"status": "running", "uptime": 123456}
    mock_tasks = []
    mock_proxmox_api.return_value.nodes.return_value.status.get.return_value = mock_status
    mock_proxmox_api.return_value.nodes.return_value.tasks.get.return_value = mock_tasks
    
    response = client.get("/mcp/context/node/test-node")
    assert response.status_code == 200
    assert response.json()["status"] == mock_status

def test_get_vm_info(mock_proxmox_api):
    """Test getting information about a specific VM."""
    mock_vm_info = {"status": "running", "name": "test-vm"}
    mock_vm_config = {"cores": 2, "memory": 2048}
    mock_proxmox_api.return_value.nodes.return_value.qemu.return_value.status.current.get.return_value = mock_vm_info
    mock_proxmox_api.return_value.nodes.return_value.qemu.return_value.config.get.return_value = mock_vm_config
    
    response = client.get("/mcp/context/vm/100")
    assert response.status_code == 200
    assert response.json()["status"] == mock_vm_info
