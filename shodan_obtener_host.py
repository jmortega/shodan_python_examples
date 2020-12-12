#!/usr/bin/env python

import requests

SHODAN_API_KEY = ""
ip = '8.8.8.8'

def ShodanInfo(ip):
    try:
        result = requests.get('https://api.shodan.io/shodan/host/'+ip+'?key='+SHODAN_API_KEY+'&minify=True').json()
    except Exception as exception:
        result = {"error":"Informacion no disponible."}
    return result

print(ShodanInfo(ip))
