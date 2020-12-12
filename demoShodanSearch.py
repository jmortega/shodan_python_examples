#!/usr/bin/env python

import shodan
import argparse
import socket

SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Shodan search')
    
# Parámetros
parser.add_argument("-target", dest="target", help="target IP / domain", required=True)
parser.add_argument("-search", dest="search", help="search", required=None)

parsed_args = parser.parse_args()

hostname = socket.gethostbyname(parsed_args.target)

# Realizar la solicitud en un bloque try / except para detectar errores
try:
        # Buscar en Shodan con el objeto api
        results = api.search(parsed_args.search)

        # mostrar los resultados
        print('Resultados: %s' % results['total'])
        for result in results['matches']:
                print('IP: %s' % result['ip_str'])
                print(result['data'])
                print('')
				
except shodan.APIError as exception:
        print('Error: %s' % exception)
        
# Realizar la solicitud en un bloque try / except para detectar errores
try:
        # Buscar en Shodan con el objeto api
        results = api.count(parsed_args.search)
        
        # mostrar los resultados
        print('Resultados: %s' % results['total'])
        for result in results['matches']:
                print('IP: %s' % result['ip_str'])
                print(result['data'])
                print('')
except shodan.APIError as exception:
        print('Error: %s' % exception)       

#Busqueda por host
host = api.host(hostname)
        
# Info general
print("""
                IP: %s
                Organization: %s
                Operating System: %s
        """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        
# Imprimir banners
for item in host['data']:
        print("""Port: %s
        Banner: %s""" % (item['port'], item['data']))
