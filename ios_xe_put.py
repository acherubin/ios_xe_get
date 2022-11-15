import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

basic = HTTPBasicAuth('admin', 'cisco')
headers = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

body= '{"ietf-interfaces:interface": {"name": "GigabitEthernet2", "description": "Configured by RESTCONF", "type": "iana-if-type:ethernetCsmacd", "enabled": true}}'

x = requests.put("https://192.168.10.3/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2", auth=basic, headers=headers, data=body, verify=False)

print(x.status_code)
