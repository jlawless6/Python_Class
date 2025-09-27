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

# My answers to Exercise 3
# Read in json file
json_file = "nxos_interfaces.json"
with open(os.path.join(cwd, json_file), 'r') as f:
    intf_data = json.load(f)
pprint(intf_data)

# Create IPV4 list and IPV6 list
ipv4_list = []
ipv6_list = []

for intf, properties in intf_data.items():
    if 'ipv4' in properties.keys():
        for ip, prefix_dict in properties['ipv4'].items():
            ipv4_list.append(f"{ip}/{prefix_dict['prefix_length']}")
    if 'ipv6' in properties.keys():
        for ip, prefix_dict in properties['ipv6'].items():
            ipv6_list.append(f"{ip}/{prefix_dict['prefix_length']}")

pprint("IPv4 Addresses")
pprint("============")
pprint(ipv4_list)
print()
pprint("IPv6 Addresses")
pprint("============")
pprint(ipv6_list)

## Sample solution to Exercise 3
# filename = "nxos_interfaces.json"
# with open(filename) as f:
#     nxos_data = json.load(f)

# ipv4_list = []
# ipv6_list = []

# for intf, ipaddr_dict in nxos_data.items():
#     for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
#         for ip_addr, prefix_dict in addr_info.items():
#             prefix_length = prefix_dict["prefix_length"]
#             if ipv4_or_ipv6 == "ipv4":
#                 ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
#             elif ipv4_or_ipv6 == "ipv6":
#                 ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

# print("\nIPv4 Addresses: {}\n".format(ipv4_list))
# print("\nIPv6 Addresses: {}\n".format(ipv6_list))