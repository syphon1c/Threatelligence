#######
# Author: Gareth Phillips
# 
#
#
#
#
#
######

Basic Requirements
==================

- Ubuntu (tested on Ubuntu 12)
- Python 2.7.*
- Apache

Should run on most *nix platforms and MacOSX

Threatelligence is built ontop of the  following projects:

- Elasticsearch - http://www.elasticsearch.org
- Kibana        - http://www.elasticsearch.org/overview/kibana/


By now you should have downloaded the the threatelligence.zip file, unzip it and we will get back to it shortly.


## Installation - Elasticsearch

To install Elasticsearch on Ubuntu 12+ you will need to add the Elasticsearch public key by running the following command:

	sudo wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -


### APT based systems:


Then on APT based systems you will need to add the following to the sources.list to use the Elasticsearch repositories (use  your preffered editor):

	deb http://packages.elasticsearch.org/elasticsearch/1.0/debian stable main

Then run "apt-get update" to refresh the repositories. Then to install use "apt-get install elasticsearch"

### YUM based systems:


On YUM systems add the following to your "/etc/yum.repos.d/" directory:

	[elasticsearch-1.0]
	name=Elasticsearch repository for 1.0.x packages
	baseurl=http://packages.elasticsearch.org/elasticsearch/1.0/centos
	gpgcheck=1
	gpgkey=http://packages.elasticsearch.org/GPG-KEY-elasticsearch
	enabled=1

Once Elasticsearch is installed you should be able to run it from services if its not already running. 

	/etc/init.d/elasticsearch start

### Important Notice!

Elasticsearch requires Java to run, you will need to make sure you have the latest Java runtimes installed, add the following Java repository:

	sudo add-apt-repository ppa:webupd8team/java

Then update APT and install:
	
	sudo apt-get update
	sudo apt-get install oracle-java7-installer


Also by default Elasticsearch listens on localhost port 9200, you can edit  configuration file to make it listen on all interfaces so it can 
be accessed remotely (needed if you want to access dashboards remotely.).

	 /etc/elasticsearch/elasticsearch.yml

There is documentation on the interwebs regarding the security and hardening of Elasticsearch.

## Python Requirements: 

Elasticsearch Python Client, run the following commands to install:

	apt-get install python-pip
	pip install elasticsearch

Install Python GEOIP API:

	pip install pygeoip

Also download the Maxmind GeoLite City (free version), unless you have the more accurate paid for version:

	wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz

unzip the Geo City database and place it under the following location:

	cp geolitecity.dat threatelligence/geoip/


## Lets get everything running

Now we will get everything put in the correct locations (I have done this with my own user permissions, set yours as you choose):

	mkdir /opt/threatelligence/
	mv threatelligence/* /opt/threatelligence

Now for the Kibana based dashbaords, I have included a pre-built kibana dashboard or two for threatelligence, you can use the one included in 
this source or feel free to download a fresh one from Elasticsearch:

	mv threatelligence-dashboards/ /var/www/

You should now be able to browse to the dashboard using your browser. The data should be empty as we have not fetched data from any sources yet.

### Cron

To start fetching data, you can do this manually by running a python script or run it inside cron. Add the following cron jobs:
	
	0 */2 * * * /usr/bin/python /opt/threatelligence/cron/threatelligence_cron.py >/tmp/threatelligence_fetch.log
	0 */3 * * * /usr/bin/python /opt/threatelligence/cron/ti_clean.py >/tmp/threatelligence_clean.log

The first line in our cron jobs will fetch data from sources every 2 hours. The second line will clean out old logs every 3 hours, also
the cleaner will remove old data. Kept data is configured within the following file:

	/opt/threatelligence/threatelligence.ini

Just specify the number of days data you would like to keep, the default is set to 7 days, anthing older will be removed from the database.

### Manual

You can manually run feeds to test and grab specific feeds or test test your own custom feeds. 

	cd /opt/threatelligence/bin
	python ti_fetcher.py -i /opt/threatelligence/etc/botnet_feeds.ini

All feed configurations reside in the /opt/threatelligence/etc/ directory. You can copy a sample .ini file and customise it to fetch additional/custom feeds.
I tried to make it as simple as possible. Also all you have to do is create the ini file, leave it in the folder and the cron job will pick it up automagically.


## Completed

Once everything is running you should be able to refresh the dashboards and data should hopefully start showing. I have created two basic dashboards but you
can create, edit and go crazy.

Feel free to modify, rewrite or whatever just keep sharing should you find this useful in anyways.







