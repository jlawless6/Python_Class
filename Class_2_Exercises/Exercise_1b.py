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


output = net_connect.send_command("ping", strip_prompt=False, expect_string=r"Protocol") + "\n"
output += net_connect.send_command("\n", strip_prompt=False, expect_string=r"Target IP address") + "\n"
output += net_connect.send_command("8.8.8.8", strip_prompt=False, expect_string=r"Repeat count") + "\n"
output += net_connect.send_command("\n", strip_prompt=False, expect_string=r"Datagram size") + "\n"
output += net_connect.send_command("\n", strip_prompt=False, expect_string=r"Timeout in seconds") + "\n"
output += net_connect.send_command("\n", strip_prompt=False, expect_string=r"Extended commands") + "\n"
output += net_connect.send_command("n", strip_prompt=False, expect_string=r"Sweep range of sizes") + "\n"
output += net_connect.send_command("\n", strip_prompt=False, expect_string=r"Success rate is") + "\n"
print(output)

net_connect.disconnect()
