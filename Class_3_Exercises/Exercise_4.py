#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
from pprint import pprint
import yaml
import os
import re
import json

home_dir = os.path.expanduser("~")
cwd = os.path.dirname(os.path.abspath(__file__))

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

#####################################################################

with open(os.path.join(cwd, 'arista_arp.json'), 'r') as f:
    arp_data = json.load(f)

arp_dict = {entry['address']: entry['hwAddress'] for entry in arp_data["ipV4Neighbors"]}

pprint(arp_dict)
