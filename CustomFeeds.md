## Custom Feeds

Threatelligence uses feed configuration files to fetch data from HTTP/HTTPS sources on the Interwebs. The configuration (.ini) files have a number of options to tell the fetcher where the data is, what the data is and how to parse the data.

Example configuration file:

	[Blocklist_DE]
	url: http://www.blocklist.de/lists/bots.txt
	feed_name: BlocklistDE_Botnet
	temp_file: /tmp/blocklist_bots_tmp
	final_file: /tmp/blocklist_bots_sorted
	regex: \d{1,3}(?:\.\d{1,3}){3}
	regex_value: ipaddress
	severity: high
	type: botnet

Explanation:

        [<Feed_name>]
        url: <URL source where the data resides>
        feed_name: <feed_name>
        temp_file: <write files to this location, must end with _tmp>
        final_file: <after parsing, for debugging writes details to his file>
        regex: \d{1,3}(?:\.\d{1,3}){3} <our regex to extract the data, IP address>
        regex_value: <we must tell the parser if this is an ipaddress, domain or url>
        severity: <giving it a severity risk according to source>
        type: <type of data could be botnet, CnC, malware_domain,APT,malware_distribution,malware_ip,bruteforce,scanning,spamming> Add your own

I have sort of grouped the types to specific .ini files but you cn either add to a file or create a new one. All .ini files in the folder are automatically picked up by the cron job so no further needing to configure. 

There is a test script that you can use to test your custom feeds configuration:

	cd /opt/threatelligence/bin/
	python test_feed.py -i /opt/threatelligence/etc/apt_feeds.ini

Data will be printed to screen and logged to the file_file location, feel free to modify as you please.
