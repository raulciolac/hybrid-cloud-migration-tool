def get_disk_type(size_gb):
    if size_gb < 128:
        return "Standard_LRS"
    elif size_gb < 512:
        return "StandardSSD_LRS"
    else:
        return "Premium_LRS"

def generate_tf(vms):
    tf = """
provider "azurerm" {
  features {}
}
"""
    for vm in vms:
        tf += f"""
resource "azurerm_linux_virtual_machine" "{vm['name']}" {{
  name                = "{vm['name']}"
  location            = "West Europe"
  resource_group_name = "terraform-rg"
  size                = "Standard_B2s"
  admin_username      = "azureuser"
  network_interface_ids = []
  os_disk {{
    caching              = "ReadWrite"
    storage_account_type = "{get_disk_type(vm['disks'][0]['size_gb']) if vm['disks'] else 'Standard_LRS'}"
  }}
}}
"""
        for i, disk in enumerate(vm["disks"]):
            tf += f"""
resource "azurerm_managed_disk" "{vm['name']}_disk_{i}" {{
  name                 = "{vm['name']}-disk-{i}"
  location             = "West Europe"
  resource_group_name  = "terraform-rg"
  storage_account_type = "{get_disk_type(disk['size_gb'])}"
  disk_size_gb         = {disk['size_gb']}
  create_option        = "Empty"
}}
"""
    return tf
