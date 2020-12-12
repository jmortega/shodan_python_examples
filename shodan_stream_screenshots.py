#!/usr/bin/env python

import shodan

SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)

for banner in api.stream.banners():
    if 'opts' in banner and 'screenshot' in banner['opts']:
        # All the images are JPGs for now
        # Create the file name using its IP address
        filename = '{}/{}.jpg'.format(output_folder, banner['ip_str'])
        # Create the file itself
        output = open(filename, 'w')
        # The images are encoded using base64
        output.write(banner['opts']['screenshot']['data'].decode('base64'))

