import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

basic = HTTPBasicAuth('cisco', 'cisco')
headers = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}


x = requests.get("https://192.168.0.82/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/primary", auth=basic, headers=headers, verify=False)   

#print(x.text)
#print(x.json())
jsonResponse=x.json()

print('Interface GigabitEthernet2')
print(f'IP Address: {jsonResponse["Cisco-IOS-XE-native:primary"]["address"]}')
print(f'Subnet Mask: {jsonResponse["Cisco-IOS-XE-native:primary"]["mask"]}')