#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
from pprint import pprint

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


net_connect = ConnectHandler(**inventory['cisco4'])

version_data = net_connect.send_command("show version", use_textfsm=True)
pprint(version_data)

print(net_connect.find_prompt())

lldp_data = net_connect.send_command("show lldp neighbors detail", use_textfsm=True)
pprint(lldp_data)

print(net_connect.find_prompt())

print('neighbor interface:', lldp_data[0]['neighbor_interface'])

net_connect.disconnect()
