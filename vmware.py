from pyVim.connect import SmartConnectNoSSL
from pyVmomi import vim
import json

def connect():
    with open("config.json") as f:
        config = json.load(f)
    si = SmartConnectNoSSL(
        host=config["vcenter"],
        user=config["user"],
        pwd=config["password"]
    )
    return si

def get_vms():
    si = connect()
    content = si.RetrieveContent()
    container = content.rootFolder
    view = content.viewManager.CreateContainerView(
        container, [vim.VirtualMachine], True
    )
    vms = []
    for vm in view.view:
        disks = []
        for device in vm.config.hardware.device:
            if isinstance(device, vim.vm.device.VirtualDisk):
                disks.append({
                    "size_gb": device.capacityInKB // (1024 * 1024),
                    "datastore": device.backing.datastore.name
                })
        vms.append({
            "name": vm.name,
            "cpu": vm.config.hardware.numCPU,
            "memory": vm.config.hardware.memoryMB,
            "disks": disks
        })
    return vms
