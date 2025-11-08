import xmltodict
from lxml import etree
import xml.etree.ElementTree as ET
import os
from pprint import pprint

home_dir = os.path.expanduser("~")

cwd = os.path.dirname(os.path.abspath(__file__))

def read_xml_file(file_name):
    with open(os.path.join(cwd, file_name), 'r') as f:
        return xmltodict.parse(f.read())

def read_xml_file_forcelist(file_name, force_list=None):
    with open(os.path.join(cwd, file_name), 'r') as f:
        if force_list is None:
            force_list = {}
        else:
            force_list = {force_list: True}
        data = xmltodict.parse(f.read(), force_list=force_list)
        return data

sec_zones = read_xml_file('show_security_zones.xml')

sec_zone_single = read_xml_file_forcelist('show_security_zones_single_trust.xml', 'zones-security')


pprint(sec_zones)
pprint(sec_zone_single)