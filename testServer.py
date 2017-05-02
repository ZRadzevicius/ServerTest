#! /usr/bin/python
#Zilvinas Radzevicius
#Change
import sys
import argparse
import urllib2
import socket
import re

parser = argparse.ArgumentParser(description='These are the arguments that must be supplied')
parser.add_argument("-p", help="webserver port", required=True, type=int)
parser.add_argument("-t", help="text to check in the body ", required=True)
parser.add_argument('url', help="url of the website ", action="store")
args = parser.parse_args()

text = args.t
port = args.p
url = args.url

try:
    #create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print "FAIL"
    sys.exit(1)

try:
    #get the IP address of the host
    host_ip = socket.gethostbyname(url)
except socket.gaierror:
    #cant resolve host
    print "FAIL" 
    sys.exit(1)

try:
    #connecting to host with port specified
    s.connect((host_ip,port))
except socket.timeout:
    print "FAIL"
    sys.exit(1)

try:
    #Get content of the website
    website = urllib2.urlopen('http://' + url).read()
except urllib2.URLError:
    print "FAIL"
    sys.exit(1)

#checking if text exists in website's content
matches = re.findall(text, website);
if len(matches) == 0:
    print "FAIL"
    sys.exit(1)
else:
    print "OK"
    sys.exit(0)
