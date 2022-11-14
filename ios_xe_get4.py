import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

basic = HTTPBasicAuth('admin', 'cisco')
headers = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}


x = requests.get("https://192.168.10.3/restconf/data/Cisco-IOS-XE-native:native/hostname", auth=basic, headers=headers, verify=False)

#x = requests.get("https://192.168.10.3/restconf/", auth=basic, verify=False)
#print(x.status_code)
print(x.text)

#print (x.json())
