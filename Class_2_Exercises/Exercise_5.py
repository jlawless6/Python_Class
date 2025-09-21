#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
from datetime import datetime

home_dir = os.path.expanduser("~")

def load_yaml_to_dict(file_path):
    with open(file_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
            return data
        except yaml.YAMLError as e:
            print(f"Error loading YAML file: {e}")
            return None

filename = ".netmiko.yml"
inventory = load_yaml_to_dict(os.path.join(home_dir, filename))

nxos1 = inventory['nxos1']
nxos2 = inventory['nxos2']

net_connect = {}

for device in (nxos1, nxos2):
    net_connect[f"{device['host']}"] = ConnectHandler(**device)
    output = net_connect[f"{device['host']}"].send_config_from_file("vlan_config.txt")
    print(output)
    net_connect[f"{device['host']}"].save_config()
    net_connect[device['host']].disconnect()