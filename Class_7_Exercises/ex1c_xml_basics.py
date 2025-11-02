from lxml import etree
import os

home_dir = os.path.expanduser("~")

cwd = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(cwd, 'show_security_zones.xml'), 'r') as f:
    xml_data = f.read()

root = etree.fromstring(xml_data)

print(root.tag)
print(len(root))
