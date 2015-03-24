import json
import os
import requests
from StringIO import StringIO
from PIL import Image
from requests.exceptions import ConnectionError
def Image_Scraping(query):
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + query + '&start=%d'
    if not os.path.exists('images/'+query):
        os.makedirs('images/'+query)
    d=1
    start = 0
    while start < 60: 
        json_url = requests.get(BASE_URL % start)
        for image_info in json.loads(json_url.text)['responseData']['results']:
            url = image_info['unescapedUrl']
            print url
            try:
                image = requests.get(url,verify=False,timeout=1000)
                print "connection established"
            except ConnectionError, e:
                print 'could not download %s' % url
                continue
            filename = 'images/'+query+'/image'+str(d)+".jpg"      
            fp = open(filename,'w')
            try:
                print "Saving " +str(d) + " image" 
                Image.open(StringIO(image.content)).save(fp, 'JPEG')
            except IOError, e:
                print "cannot be saved"
                continue
            finally:
                fp.close()
            d=d+1
        start=start+4
print 'enter url'
query = raw_input()
Image_Scraping(query)
