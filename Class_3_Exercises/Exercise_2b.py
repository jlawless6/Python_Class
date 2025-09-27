#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
from pprint import pprint
import yaml
import os
import re

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

inv_key_list = [{k: v} for k, v in inventory.items() if re.search(r'[a-z]+[0-9]', k)]
inv_list = []
for dict in inv_key_list:
    for k, v in dict.items():
        inv_list.append(v)
        inv_list[-1]['host'] = k
pprint(inv_list)

# store inv_list as a yaml file
with open(os.path.join(cwd, 'inventory.yml'), 'w') as f:
    yaml.dump(inv_list, f, default_flow_style=False)
#####################################################################