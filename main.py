import click
from vmware import get_vms
from terraform import generate_tf
import os

@click.group()
def cli():
    pass

@cli.command()
def discover():
    vms = get_vms()
    for vm in vms:
        print(vm)

@cli.command()
def generate():
    vms = get_vms()
    tf = generate_tf(vms)
    with open("output/main.tf", "w") as f:
        f.write(tf)
    print("Terraform file generated in output/main.tf")

@cli.command()
def deploy():
    os.system("cd output && terraform init")
    os.system("cd output && terraform apply -auto-approve")

if __name__ == "__main__":
    cli()
