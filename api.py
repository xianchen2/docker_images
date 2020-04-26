import sodapy
import json
import sys
import os



def get_data(page_size, num_pages=None, output=None):
    
    client = sodapy.Socrata('data.cityofnewyork.us', os.environ['APP_KEY'])
    if num_pages == None:
        r = client.get('nc67-uf89', limit=page_size)
    else:
        r = client.get('nc67-uf89', limit=page_size, offset=(num_pages - 1) * page_size)
    
    if output == None:
        print(r)
    else:
        with open(output+'.txt', 'w') as outfile:
            json.dump(r, outfile)
