import requests
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

basic = HTTPBasicAuth('admin', 'cisco')

x = requests.get("https://192.168.10.3/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1", auth=basic, verify=False)

#x = requests.get("https://192.168.10.3/restconf/", auth=basic, verify=False)
#print(x.status_code)
print(x.text)
