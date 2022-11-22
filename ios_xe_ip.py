import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

basic = HTTPBasicAuth('cisco', 'cisco')
headers = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

body= '{"Cisco-IOS-XE-native:primary": {"address": "192.168.100.1", "mask": "255.255.255.0"}}'

x = requests.put("https://192.168.0.82/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/primary", auth=basic, headers=headers, data=body, verify=False)

print(x.status_code)