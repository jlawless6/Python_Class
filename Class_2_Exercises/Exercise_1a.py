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


net_connect = ConnectHandler(**inventory['cisco4'])


output = net_connect.send_command_timing("ping", strip_prompt=False) + "\n"
output += net_connect.send_command_timing("\n", strip_prompt=False) + "\n"
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False) + "\n"
output += net_connect.send_command_timing("\n", strip_prompt=False) + "\n"
output += net_connect.send_command_timing("\n", strip_prompt=False) + "\n"
output += net_connect.send_command_timing("\n", strip_prompt=False) + "\n"
output += net_connect.send_command_timing("n", strip_prompt=False) + "\n"
output += net_connect.send_command_timing("\n", strip_prompt=False) + "\n"
print(output)

net_connect.disconnect()
