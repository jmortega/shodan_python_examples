#!/usr/bin/env python

import shodan
import requests

SHODAN_API_KEY = ""
api = shodan.Shodan(SHODAN_API_KEY)

target = 'www.python.org'

dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + SHODAN_API_KEY


try:
    # Primero necesitamos resolver nuestro dominio a una IP
    resolved = requests.get(dnsResolve)
    hostIP = resolved.json()[target]
    print(hostIP)
   

    # Entonces necesitamos hacer una búsqueda de Shodan en esa IP
    host = api.host(hostIP)
    #print(host)
    print("IP: %s" % host['ip_str'])
    print("Organization: %s" % host.get('org', 'n/a'))
    print("Operating System: %s" % host.get('os', 'n/a'))


    # Imprimir todos los banners
    for item in host['data']:
        print("Port: %s" % item['port'])
        print("Banner: %s" % item['data'])
        
                
except shodan.APIError as exception:
        print('Error: %s' % exception)
