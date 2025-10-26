#!/home/jlawless/ VENV/py3_venv/bin/python

import yaml
import os

home_dir = os.path.expanduser("~")

def get_device_info(device_name):
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
    device_info = inventory.get(device_name)
    if not device_info:
        print(f"Device '{device_name}' not found in inventory.")
        return None

    return device_info


def print_ip_mac_addresses(output):
    output_dicts = output[0]['result']['ipV4Neighbors']
    for dict in output_dicts:
        print(f"IP Address: {dict['address']}, MAC Address: {dict['hwAddress']}")
