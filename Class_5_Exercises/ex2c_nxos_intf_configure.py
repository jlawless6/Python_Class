#!/home/jlawless/ VENV/py3_venv/bin/python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
import my_devices
from netmiko import ConnectHandler

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/exercise2')

nxos1 = my_devices.inventory['nxos1']
nxos2 = my_devices.inventory['nxos2']

net_connect = ConnectHandler(**nxos1)
output = net_connect.send_command("show ip interface brief")

print(output)

# template_file = 'nxos_intf_bgp.j2'
# template = env.get_template(template_file)
# output = template.render(**router_vars)
# print(output)









# #######################################################

# from netmiko import ConnectHandler
# import yaml
# import os
# from datetime import datetime

# home_dir = os.path.expanduser("~")

# def load_yaml_to_dict(file_path):
#     with open(file_path, 'r') as f:
#         try:
#             data = yaml.safe_load(f)
#             return data
#         except yaml.YAMLError as e:
#             print(f"Error loading YAML file: {e}")
#             return None

# filename = ".netmiko.yml"
# inventory = load_yaml_to_dict(os.path.join(home_dir, filename))

# start_time = datetime.now()

# net_connect = ConnectHandler(**inventory['cisco3'], fast_cli=True)

# commands = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

# output = net_connect.send_config_set(commands)

# print()
# print("*" * 80)
# print(output)
# print("*" * 80)
# print()

# ping_result = net_connect.send_command("ping 8.8.8.8")

# if "!!!!!" in ping_result:
#     print("Ping successful")
# else:
#     print("Ping failed")

# net_connect.disconnect()

# end_time = datetime.now()
# print(f"Total time: {end_time - start_time}")