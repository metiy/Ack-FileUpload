import requests
import sys

VERIFY   = False #REMOVE WHEN SSL CERTIFICATES ARE OK
HTTPS    = True
HEADERS  = {'Content-Type': 'multipart/form-data'}
TARGET   = "localhost/upload"

if (len(sys.argv) > 2 or len(sys.argv) == 1):
    print ("[-] Usage : \"python client.py file\"")
    sys.exit(1)

try:
    files = {'filearg': open(sys.argv[1], 'rb')}
    protocol = "https://" if (HTTPS) else "http://" 
    r = requests.post(protocol + TARGET, files=files, verify=VERIFY)
    print(r.text)
except IOError as e :
    print ("[-] IOError : {1}".format(e.errno, e.strerror))
