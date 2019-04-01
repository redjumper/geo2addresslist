#!/usr/bin/python

import csv
import urllib2
import zipfile
import os
from urllib2 import urlopen

def download_db():

	url = "https://geolite.maxmind.com/download/geoip/database/GeoLite2-ASN-CSV.zip"
	file = "GeoLite2-ASN-CSV.zip"
	
	response = urlopen(url)
	CHUNK = 16 * 1024
	with open(file, 'wb') as f:
		while True:
			chunk = response.read(CHUNK)
			if not chunk:
				break
			f.write(chunk)
			
	zip_ref = zipfile.ZipFile(file, 'r')
	zip_ref.extractall()
	zip_ref.close()

	os.system("rm -f GeoLite2-ASN-CSV.zip && mv GeoLite*/* . && rm -f GeoLite2-ASN-Blocks-IPv6.csv && rm -f COPYRIGHT.txt LICENSE.txt && rm -rf GeoLite*/")
	
def parse_organization():

	with open("freedom-addresslist.rsc", 'w') as f:
		f.write("/ip firewall address-list")
		f.write("\n")
		f.write("remove [find list=freedom]")
		f.write("\n")
		
	with open("organization.txt", 'r') as f:
		for line_terminated in f:
			line = line_terminated.rstrip('\n')
			generate_addresslist(line)

def generate_addresslist(organization):

	with open("freedom-addresslist.rsc", 'a') as f:
		#read csv, and split on "," the line
		asn_ipv4 = csv.reader(open('GeoLite2-ASN-Blocks-IPv4.csv', "r"), delimiter=",")
		#loop through csv list
		for row in asn_ipv4:
			#if current rows 2nd value is equal to input, print that row
			if row[2].upper().startswith(organization.upper()):
				f.write("add address=" + row[0] + " comment=\"" + row[2] + "-AS" + row[1] + "\" list=freedom")
				f.write("\n")
				
if __name__ == '__main__':

	download_db()
	parse_organization()