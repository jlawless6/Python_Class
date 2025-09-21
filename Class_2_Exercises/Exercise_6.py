#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
import time

home_dir = os.path.expanduser("~")

# get current working directory of this python file
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


cisco4 = inventory['cisco4']
cisco4['secret'] = cisco4['password']
cisco4['session_log'] = os.path.join(cwd, "my_output.txt")

net_connect = ConnectHandler(**cisco4)

print(f'original prompt:\n{net_connect.find_prompt()}\n\n')

net_connect.config_mode()
print(f'In config mode?\n{net_connect.find_prompt()}\n\n')

net_connect.exit_config_mode()
print(f'After exiting config mode:\n{net_connect.find_prompt()}\n\n')

net_connect.write_channel('disable\n')
time.sleep(2)
print(f'After sending disable:\n{net_connect.read_channel()}\n\n')

net_connect.enable()
print(f'After re-entering enable mode:\n{net_connect.find_prompt()}\n\n')

net_connect.disconnect()
