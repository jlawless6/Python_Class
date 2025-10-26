#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
from pprint import pprint
import pyeapi
from my_funcs import get_device_info, print_ip_mac_addresses

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


###########################################################################################

arista3 = get_device_info('arista3')

host = arista3['host']
usrname = arista3['username']
password = arista3['password']

connection = pyeapi.client.connect(
    transport='https',
    host=host,
    username=usrname,
    password=password,
    port=443
)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

print_ip_mac_addresses(output)