#!/usr/bin/env python

import shodan

SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)

def has_vuln(banner, vuln):
    if 'vulns' in banner['opts'] and vuln in banner['opts']['vulns']:
        return True
    return False

for banner in api.stream.banners():
    if has_vuln(banner, 'CVE-2020-0796'):
        print(banner)


