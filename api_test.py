
import json
import urllib
from urllib2 import urlopen
import urlparse
import ssl

# Note that Google is increasingly requiring keys
# for this API
#
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl +  urllib.urlencode(
        {'address': address})

    print('Retrieving', url)

    import ssl

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    data =urlopen(url, context=ctx).read().decode()

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    #lat = js["results"][0]["geometry"]["location"]["lat"]
    #lng = js["results"][0]["geometry"]["location"]["lng"]
    #print('lat', lat, 'lng', lng)
    #location = js['results'][0]['formatted_address']
    #print(location)
    print js["results"][0]['place_id']
     