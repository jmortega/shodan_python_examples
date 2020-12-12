#!/usr/bin/env python

import shodan

SHODAN_API_KEY = ""
host = ""

api = shodan.Shodan(SHODAN_API_KEY)

#Busqueda por host
host = api.host(host)

#obtener vulnerabilidades y exploits
if host['vulns'] is not None:
    for item in host['vulns']:
        CVE = item.replace("!","")
        print("Vuln:",CVE)        
        try:
            exploits = api.exploits.search(CVE)
            for item in exploits['matches']:
                print(item.get('description'))
        except:
            pass
            
