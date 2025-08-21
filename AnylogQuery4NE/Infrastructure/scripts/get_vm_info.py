from nativeedge import ctx
from nativeedge.exceptions import NonRecoverableError
import shutil


vm_node_id = ctx.source.instance.id
vm_ip_localpath = f'/tmp/{vm_node_id}/ip'
vm_mac_localpath = f'/tmp/{vm_node_id}/mac'
addresses = []
for path in [vm_ip_localpath, vm_mac_localpath]:
    with open(path) as file:
        content = file.read()
        addresses.append(content.strip())

ctx.source.instance.runtime_properties['ip'] = \
    str(addresses[0])
ctx.source.instance.runtime_properties['capabilities'] = {}
ctx.source.instance.runtime_properties['capabilities']['vm_public_mac'] = \
    str(addresses[1])

if ctx.target.node.id == 'vm_ssh_proxy':
    ctx.source.instance.runtime_properties['capabilities']['vm_host'] = \
        ctx.target.instance.runtime_properties['eo_proxy_url']
    ctx.source.instance.runtime_properties['capabilities']['vm_ssh_port'] = \
        ctx.target.instance.runtime_properties['eo_proxy_port']
    ctx.source.instance.runtime_properties['capabilities']['vm_public_ip'] = \
        str(addresses[0])
else:
    raise NonRecoverableError('Invalid target node.')

# Clean up temp file
vm_ip_localpath = f'/tmp/{vm_node_id}'
try:
    shutil.rmtree(vm_ip_localpath)
except Exception as removal_error:
    ctx.logger.error(
        f'{vm_node_id} temp files removal error: {removal_error}')
