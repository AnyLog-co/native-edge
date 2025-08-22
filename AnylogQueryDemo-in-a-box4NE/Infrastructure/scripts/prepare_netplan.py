from nativeedge import ctx
from nativeedge.state import ctx_parameters as inputs
import base64
import yaml


netplan_input = inputs.get('netplan_input')
netplan_yaml = yaml.dump(netplan_input)
netplan_raw = f"""#cloud-config
{netplan_yaml}"""

netplan_encoded = base64.b64encode(netplan_raw.encode('utf-8'))

ctx.instance.runtime_properties['netplan_raw'] = netplan_raw
ctx.instance.runtime_properties['netplan_encoded'] = netplan_encoded.decode('utf-8')