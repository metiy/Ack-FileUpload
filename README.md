



## Server

PORT               -> Server listening port, this should match the Nginx configuration file.
UPLOADS            -> Upload directory
DEBUG              -> Set this to True for verbose to view requests content
SECURITY_RANDOMIZE -> Store 
ADD_TIME_TO_FILE   = True #Only for not randomized



## Client

Usage : python client.py FILE

Script Variables :

VERIFY   -> Certificate Verification, set this to false only for testing purpose.
HTTPS    -> True : use HTTPS, False : use HTTP
HEADERS  -> Post request headers
TARGET   -> Server address
