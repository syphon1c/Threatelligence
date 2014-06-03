###
# Description: This is the test script that reads custome configuration files
#              fetches sources, parses and prints to screen for your debug
# Author:      Gareth Phillips
# Version:     0.1
# License:     GNU/GPL
##
import os
import ConfigParser
import argparse
import datetime
import urllib
import filecmp
import glob
import time
import re
import ConfigParser
import pygeoip
import socket
import argparse
import hashlib

parser = argparse.ArgumentParser(description='This is a geenric test script for fetching custom feed data')
parser.add_argument('-i','--input', help='Input file .ini name',required=True)
args = parser.parse_args()

# Input file - the ini files setup in etc/
ParserConfig = args.input

# Prepare configuration parsers
Config = ConfigParser.ConfigParser()
Config.read(ParserConfig)

currdate = datetime.date.today()

def extract_ips(data):
    return re.findall(feed_regex, data)

def fetcher():
	if os.path.isfile(temp_file):
		print "file exists, processing: " + temp_file
	else:
    		try:
			urllib.urlretrieve(fetch_url, temp_file)
    		except:
			print "Could not access:" + fetch_url
			print "Check that you can access the url!"
        		return 
		drop_file = False


if __name__ == '__main__':
	for feed_config in Config.sections():
        	config_name = feed_config
        	print "Working on the following config feed: ",feed_config
        	fetch_url = Config.get(config_name,'url')
        	parser_name = Config.get(config_name,'feed_name')
        	temp_file = Config.get(config_name,'temp_file')
        	process_file = Config.get(config_name,'final_file')
        	feed_regex = Config.get(config_name,'regex')
		data_type = Config.get(config_name,'regex_value')
        	result_type = Config.get(config_name,'type')
		severity = Config.get(config_name,'severity')
		print "fetching feed from: ", fetch_url
		fetcher()
		
		gi = pygeoip.GeoIP('/opt/threatelligence/geoip/GeoLiteCity.dat')		

		if (data_type == "ipaddress"):
			try:
				with open(temp_file) as infile, open(process_file, "w") as outfile:
   					seen = set()
    					for line in infile:
    	    					for ip in extract_ips(line):
            						if ip not in seen:
               							seen.add(ip)
								# Index a document:
								go = gi.record_by_addr(ip)
								try:
									longat = go['latitude'], go['longitude']
									ccode = go['country_code']
									ccountry = go['country_name']
								except:
									longat = ""
									ccode = ""
									ccountry = ""
								m = hashlib.md5()
								m.update(ip+parser_name)
								es_dbid = m.hexdigest()

              							print  ip, ccode, longat, result_type, parser_name
								print >>outfile, ip, ccode, parser_name, severity, result_type, longat, currdate
			except:
				print "no log file:" + temp_file

		if (data_type == "url"):
			try:
       	                 	with open(temp_file) as infile, open(process_file, "w") as outfile:
                         	       seen = set()
                         	       for line in infile:
                         	               for ip in extract_ips(line):
                         	                       if ip not in seen:
								seen.add(ip)
                         	                                ip1 = ip.replace("http://","")
								host_url = (ip1.split('/')[0]) #for ip2 in ip1.split()]
								# Index a document:
								try:
									#res = socket.getaddrinfo(host_url, None,t, socket.SOCK_STREAM)
									go = gi.record_by_name(host_url)	
								except:
									go = ""
								#print go #go = gi.country_code_by_name(host_url)
                        	                                try:
                        	                                        longat = go['latitude'], go['longitude']
                        	                                        ccode = go['country_code']
                        	                                        ccountry = go['country_name']
                        	                                except:
                        	                                        longat = ""
                        	                                        ccode = ""
                        	                                        ccountry = ""
								m = hashlib.md5()
                        	                                m.update(host_url+ip+parser_name)
								es_dbid = m.hexdigest()
                        	                                print  ip, ccode, longat, result_type, parser_name
                        	                                print >>outfile, ip, ccode, parser_name, severity, result_type, longat, currdate
			except:
                                print "no log file:" + temp_file
                if (data_type == "domain"):
			try:
	                        #gip = pygeoip.GeoIP('../geoip/GeoIP.dat')
	                        with open(temp_file) as infile, open(process_file, "w") as outfile:
       	                        	seen = set()
                                	for line in infile:
						line = line.strip()
	                                        for ip in extract_ips(line):
	                                                if ip not in seen:
	                                                        seen.add(ip)
	                                                        # Index a document:
	                                                        try:
	                                                                #res = socket.getaddrinfo(host_url, None,t, socket.SOCK_STREAM)
        	                                                        go = gi.record_by_name(ip)
                	                                        except:
                        	                                        go = ""
                                	                        #print go #go = gi.country_code_by_name(host_url)
                                        	                try:
                                                	                longat = go['latitude'], go['longitude']
                                                        	        ccode = go['country_code']
                                                                	ccountry = go['country_name']
                                                        	except:
	                                                                longat = ""
        	                                                        ccode = ""
                	                                                ccountry = ""
								m = hashlib.md5()
                                	                        m.update(ip+parser_name)
								es_dbid = m.hexdigest()
                                                        	print  ip, ccode, longat, result_type, parser_name
                                                        	print >>outfile, ip, ccode, parser_name, severity, result_type, longat, currdate
			except:
                        	print "no log file:" + temp_file
