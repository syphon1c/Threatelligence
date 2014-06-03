###
# Description: This script removes the downloaded source file and 
#              reads the config file which determines how many days of 
#	       data should be kept in elasticsearch
# Author:      Gareth Phillips
# Version:     0.1
# License:     GNU/GPL
##
import os
import ConfigParser
import argparse
from datetime import date, timedelta
import urllib
import glob
import socket
import subprocess

Config = ConfigParser.ConfigParser()
Config.read("/opt/threatelligence/threatelligence.ini")

print "Going to clean old data from elasticsearch"

days = Config.get('DataStorage','daystokeepdata')
daystokeep = int(days)
removedate = date.today()-timedelta(days=daystokeep)
removedate =str(removedate)
esUrl = "http://localhost:9200/threatelligence/_query?q=date:"+removedate
proc = subprocess.Popen(["curl", "-XDELETE", esUrl], stdout=subprocess.PIPE)
(out, err) = proc.communicate()
print "Done!"

print "Deleting old _tmp files!"
directory='/tmp/'
os.chdir(directory)
files=glob.glob('*_tmp')
for filename in files:
    os.unlink(filename)


