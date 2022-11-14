import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

basic = HTTPBasicAuth('admin', 'cisco')
headers = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

body={
  "Cisco-IOS-XE-native:hostname": "TEST"
}


x = requests.patch("https://192.168.10.3/restconf/data/Cisco-IOS-XE-native:native/hostname", auth=basic, headers=headers, json=body, verify=False)

print(x.status_code)
