# Hybrid VMware → Azure Migration Tool

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Description

This is a Python CLI tool that automates the migration of VMware virtual machines to **Microsoft Azure** using **Terraform**.  

The tool is designed to:

- Discover VMware VMs and SAN/Datastores  
- Automatically map storage to Azure disks (OS and data disks)  
- Generate Terraform configurations for Azure resources  
- Deploy VMs automatically in Azure  

This project demonstrates **cloud automation and infrastructure-as-code skills**, making it a strong portfolio project for CVs or interviews.

---

## Features

- ✅ VMware VM discovery  
- ✅ SAN / datastore detection  
- ✅ Smart storage mapping (OS + data disks)  
- ✅ Terraform file generation  
- ✅ Automatic deployment to Azure  
- 🔹 Extensible: dry-run mode, cost estimation, JSON export  

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/raulciolac/hybrid-cloud-migration-tool.git
cd hybrid-cloud-migration-tool
