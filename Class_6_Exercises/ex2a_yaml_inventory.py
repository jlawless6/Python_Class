#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
from pprint import pprint
import pyeapi

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

arista3 = {**inventory['arista3']}

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

output_dicts = output[0]['result']['ipV4Neighbors']
for dict in output_dicts:
    print(f"IP Address: {dict['address']}, MAC Address: {dict['hwAddress']}")