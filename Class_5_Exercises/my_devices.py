#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
import yaml
import os
import re
from pprint import pprint
from ciscoconfparse import CiscoConfParse
import textfsm

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
