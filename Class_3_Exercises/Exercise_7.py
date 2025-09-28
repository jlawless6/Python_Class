#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
import re
from pprint import pprint
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

bgp_config = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''
bgp_obj = CiscoConfParse(bgp_config.splitlines(), ignore_blank_lines=False)

bgp_ips = []
bgp_neighbors = bgp_obj.find_objects_w_parents(parentspec=r'^router bgp', childspec=r'neighbor')

for neighbor in bgp_neighbors:
    _, neighbor_ip = neighbor.text.split()
    for child in neighbor.children:
        if "remote-as" in child.text:
            remote_as = child.text.split()
    bgp_ips.append((neighbor_ip, remote_as))
pprint("bgp peers: ")
pprint(bgp_ips)
