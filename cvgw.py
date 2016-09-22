#!/usr/bin/python
import requests
import os
import sys

url = "https://controller:5000/v2.0/tokens"

payload = "{\"auth\": {\"passwordCredentials\": {\"username\":\"admin\", \"password\":\"asdf\"}, \"tenantName\":\"admin\"}}"
headers = {
    'content-type': "application/json",
    }

response = requests.request("POST", url, data=payload, headers=headers)

token = response.json()['access']['token']['id']
#print token

############################
url = "https://controller:9696/v2.0/vpn/gateways"

payload = "{\"gateway\": {\"router_id\": \"%s\", \"network_id\": \"%s\"}}" %(sys.argv[1], sys.argv[2])
headers = {
    'content-type': "application/json",
    'x-auth-token': "%s" % token
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
