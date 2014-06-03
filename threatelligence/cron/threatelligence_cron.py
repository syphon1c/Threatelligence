###
# Description: This is the main cron script that ikicks off the automatic
#              fetching of sources as defined in the ini files
# Author:      Gareth Phillips
# Version:     0.1
# License:     GNU/GPL
##
import os
import subprocess

def get_filepaths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  

    return file_paths  

print "Starting cronjob fetching data!"
full_file_paths = get_filepaths("/opt/threatelligence/etc/")

for f in full_file_paths:

  if f.endswith(".ini"):
     print "starting with: " + f
     inifile = f
     runfetch = "/usr/bin/python /opt/threatelligence/bin/ti_fetcher.py -i " + inifile
     subprocess.call(runfetch, shell=True)
     print "finished processing: " + f
