#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

devices = {'device1': {
    'host': "cisco3.lasthop.io",
    'username': "pyclass",
    'password': password,
    'device_type': "cisco_xe",
    # 'session_log': "my_session.txt",
    }, 'device2': {
    'host': "cisco4.lasthop.io",
    'username': "pyclass",
    'password': password,
    'device_type': "cisco_xe",
    # 'session_log': "my_session.txt",
}}

net_connect = {}
for device in devices:
    net_connect[device] = ConnectHandler(**devices[device])

for device in net_connect:
    output = net_connect[device].send_command("show ip int brief")
    print(f"\n\n{device} : {devices[device]['host']}\n")
    print(output)
    print(net_connect[device].find_prompt())

for device in net_connect:
    net_connect[device].disconnect()



# net_connect.disconnect()

