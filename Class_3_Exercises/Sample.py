#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os

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

devices = {k: v for k, v in inventory.items() if k == 'cisco3' or k == 'cisco4'}

net_connect = {}
for device in devices:
    net_connect[device] = ConnectHandler(**devices[device])

for device in net_connect:
    output = net_connect[device].send_command("show ip int brief")
    print(f"\n\n{device} : {devices[device]['host']}\n")
    print(output)
    print(net_connect[device].find_prompt())

print(f"\n\n{net_connect['cisco3'].find_prompt()}")
print(net_connect['cisco3'].send_command("show version"))

for device in net_connect:
    net_connect[device].disconnect()



# net_connect.disconnect()

