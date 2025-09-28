#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
import re
from ciscoconfparse import CiscoConfParse

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

net_connect = ConnectHandler(**inventory['cisco4'])
show_run = net_connect.send_command("show running-config")

# get running config:
config_obj = CiscoConfParse(show_run.splitlines(), ignore_blank_lines=False)

# find all interfaces with children:
intf_with_ip = config_obj.find_objects_w_child(parentspec=r"^interface",
    childspec=r"^\s+ip address")

for intf in intf_with_ip:
    print(f"\nInterface Line: {intf.text}")
    for child in intf.children:
        if re.search(r"^\s+ip address", child.text):
            print(f"IP Address Line:  {child.text}")
            print()