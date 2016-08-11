##Install
Python is required.

sudo pip3 install tornado

git clone https://github.com/Storm75/Ack-FileUpload.git

cd Ack-FileUpload && mkdir uploads

##Server

Usage : python server.py

#Script Variables

PORT               : Server listening port, this should match the Nginx configuration file

UPLOADS            : Upload directory path

VERBOSE            : Set to "True" for verbose to view requests content

SECURITY_RANDOMIZE : Set to "True" to change filenames to GUID-4.

ADD_TIME_TO_FILE   : Set to "true" to add datetime to filenames to avoid erasing, useless if SECURITY_RANDOMIZE is set to true.


## Client

Usage : python client.py FILE

#Script Variables

VERIFY    : Certificate Verification, set this to false only for testing purpose.

HTTPS     : If set to False, use only HTTP

HEADERS   : Post request headers

TARGET    : Server address


## Nginx

The tornado webserver should be connected to Nginx which should behave as a reverse-proxy for better performance.
