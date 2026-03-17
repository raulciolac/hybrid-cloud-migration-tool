# Hybrid VMware → Azure Migration Tool

## Description

This is a **Python CLI tool** that automates the migration of VMware virtual machines to **Microsoft Azure** using **Terraform**.  

The tool is designed to:  
- Discover VMware VMs and SAN/datastores  
- Automatically map storage to Azure disks (OS + data disks)  
-Generate Terraform configurations for Azure resources  
- Deploy VMs automatically in Azure  

This project demonstrates cloud automation and **Infrastructure-as-Code (IaC)** skills, making it a strong portfolio project for **CVs or interviews**.  

---

## Features

- VMware VM discovery  
- SAN / datastore detection  
- Smart storage mapping (OS + data disks)  
- Terraform file generation  
- Automatic deployment to Azure  
- Extensible: dry-run mode, cost estimation, JSON export  

---

## Setup

1. **Clone the repository:**
```bash
git clone https://github.com/raulciolac/hybrid-cloud-migration-tool.git
cd hybrid-cloud-migration-tool

2.Create and activate a Python virtual environment:
python3 -m venv venv
source venv/bin/activate

3.	Install required libraries:
pip install -r requirements.txt

4.	Repository structure (included files):
main.py          # CLI main script
vmware.py        # VMware discovery code
terraform.py     # Terraform generator
config.json      # VMware vCenter config
output/          # Folder where Terraform files will be generated
README.md        # Documentation
LICENSE          # MIT License
requirements.txt # Python dependencies

5.	Configure VMware access in config.json:
{
  "vcenter": "IP_VCENTER",
  "user": "administrator@vsphere.local",
  "password": "PASSWORD"
}

Usage
	Discover VMware VMs:
python main.py discover
	Generate Terraform files:
python main.py generate
	Deploy to Azure automatically:
python main.py deploy
    Output Terraform files are saved in the output/ folder.

Notes
	Make sure Azure CLI is installed and you are logged in (az login)
	Terraform must be installed and available in your PATH
	The tool can be extended for cost estimation, dry-run mode, or JSON export

License

This project is licensed under the MIT License – see the LICENSE￼ file for details.



