#!/home/jlawless/ VENV/py3_venv/bin/python

from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    host="cisco3.lasthop.io",
    username="pyclass",
    password=getpass(),
    device_type="cisco_xe",
    session_log="my_session.txt",
)

output = net_connect.send_command("show ip int brief")

print(output)

print(net_connect.find_prompt())
net_connect.disconnect()

