from shodan import Shodan

API_KEY=""
api = Shodan(API_KEY)

# Search for websites that have been "hacked"
for banner in api.search_cursor('http.title:"hacked by"'):
    print(banner)

# Get the total number of industrial control systems services on the Internet
ics_services = api.count('tag:ics')
print('Industrial Control Systems: {}'.format(ics_services['total']))

# Get the total number of scada services on the Internet
scada_services = api.count('tag:scada')
print('Supervisory Control and Data Acquisition: {}'.format(scada_services['total']))

# Get the total number of plc services on the Internet
plc_services = api.count('tag:plc')
print('Programmable Logic Controller: {}'.format(plc_services['total']))

# Get the total number of dcs services on the Internet
dcs_services = api.count('tag:dcs')
print('Distributed Control System: {}'.format(dcs_services['total']))
