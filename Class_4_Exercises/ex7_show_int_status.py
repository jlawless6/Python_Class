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

#####################################################################

# use txtfsm to parse the output of show int status from text file using template file

template_file = os.path.join(cwd, "ex7_show_int_status.tpl")
output_file = os.path.join(cwd, "ex7_show_int_status.txt")

template = open(template_file)
with open(output_file) as f:
    raw_output = f.read()

re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_output)

template.close()

pprint(fsm_results)

show_int_status_dict_list = [{
    'PORT_NAME': row[0],
    'STATUS': row[1],
    'VLAN': row[2],
    'DUPLEX': row[3],
    'SPEED': row[4],
    'PORT_TYPE': row[5]
    } for row in fsm_results]

pprint(show_int_status_dict_list)