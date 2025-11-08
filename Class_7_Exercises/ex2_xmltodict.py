import xmltodict
from lxml import etree
import os
from pprint import pprint

home_dir = os.path.expanduser("~")

cwd = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(cwd, 'show_security_zones.xml'), 'r') as f:
    xml_data = f.read()

data_dict = xmltodict.parse(xml_data)

trust_zone = data_dict['zones-information']['zones-security']

for item , zone in enumerate(trust_zone):
    print(f'Security Zone {item + 1}: {zone["zones-security-zonename"]}')