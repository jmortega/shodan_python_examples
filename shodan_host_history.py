#!/usr/bin/env python

import shodan
import argparse
import socket

SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Shodan host history')
    
# Parámetros
parser.add_argument("-target", dest="target", help="target IP / domain", required=True)
parsed_args = parser.parse_args()
hostname = socket.gethostbyname(parsed_args.target)

#Busqueda por host
host = api.host(hostname,history=True)
        
# Info general
print("""
                IP: %s
                Organization: %s
                Operating System: %s
        """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        
# Imprimir banners
for item in host['data']:
    print("""Port: %s Banner: %s""" % (item['port'], item['data']))
