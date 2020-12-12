#!/usr/bin/env python

import shodan
import re

sitios =[]
shodanKeyString = ''
shodanApi = shodan.Shodan(shodanKeyString)

resultados = shodanApi.search("port: 21 Anonymous user logged in")
print("numero de hosts: " + str(len( resultados['matches'])))
for resultado in resultados['matches']:
	if resultado['ip_str'] is not None:
		sitios.append(resultado['ip_str'])
		
for sitio in sitios:
    print(sitio)
