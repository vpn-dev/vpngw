#!/usr/bin/python
import requests
import os
import sys

# get token
url = "https://controller:5000/v2.0/tokens"

payload = '{"auth": {"passwordCredentials": {"username":"%s", "password":"%s", "tenantName":"%s"}}}' \
        % (os.getenv('OS_USERNAME'), os.getenv('OS_PASSWORD'), os.getenv('OS_TENANT_NAME'))
headers = {
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

token = response.json()['access']['token']['id']
print token

# create vpn gw
url = "https://controller:9696/v2.0/vpn/gateways"

payload = '{"gateway": {"router_id": "%s", "network_id": "%s"}}' % (sys.argv[1], sys.argv[2])

headers = {
    'content-type': "application/json",
    'x-auth-token': token 
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
