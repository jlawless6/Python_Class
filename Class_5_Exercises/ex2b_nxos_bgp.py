from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/exercise2')

router_vars = {'routers': {
    "nxos1": {'interface': "Ethernet1/1",
              'ip': "10.1.100.1",
              'netmask': "24",
              'peer_ip': "10.1.100.2"},
    "nxos2": {'interface': "Ethernet1/1",
              'ip': "10.1.100.2",
              'netmask': "24",
              'peer_ip': "10.1.100.1"}},
    'local_as': 22}

template_file = 'nxos_intf_bgp.j2'
template = env.get_template(template_file)
output = template.render(**router_vars)
print(output)
