# Hybrid VMware → Azure Migration Tool

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Tool CLI Python care:

- Descoperă VM-uri VMware și SAN/Datastore
- Mapare inteligentă storage → Azure Disk
- Generează Terraform configuration
- Deploy automat în Microsoft Azure

## Setup

1. Clone repo: `git clone https://github.com/raulciolac/hybrid-cloud-migration-tool.git`
2. Accesează folderul: `cd hybrid-cloud-migration-tool`
3. Creează mediu virtual: `python3 -m venv venv`
4. Activează-l: `source venv/bin/activate`
5. Instalează librării: `pip install pyvmomi click`

## Usage

- `python main.py discover` → Listează VM-uri VMware  
- `python main.py generate` → Generează Terraform files  
- `python main.py deploy` → Deploy automat în Azure

## Notes

- `config.json` trebuie completat cu date vCenter reale  
- Output Terraform se generează în folderul `output/`  
- Tool-ul poate fi extins cu cost estimation și dry-run mode

## License

MIT License
