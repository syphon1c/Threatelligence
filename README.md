
## Threatelligence v0.1

Threatelligence is a simple project I created to start learning Python which lead me to Elasticsearch and Kibana. I was playing around with some really great open source intelligence frameworks, namely collective-Intelligence Framework (CIF, you can find it on Github). After playing around I figured I wanted to do something similar except make it will be simpler and add some eye-candy to it.

Threatelligence fetches cyber threat intelligence data from various sources available on the Interwebs and feeds the data into Elasticsearch while slightly enriching it. The dashboards which are built using Kibana are used to display data and make searching through the data extremely easy.

![World Map Threat Dashboard](http://4.bp.blogspot.com/-vrDNfe3_JP8/U43KMZ3okII/AAAAAAAAAPU/E6j_KBUdLYM/s1600/Screen+Shot+2014-06-03+at+3.14.24+PM.png)


I have made made it very easy to add your own custom feeds to Threatelligence, automate the fetching of data and removing old data, see the Customfeeds.md. You should be able to add all kinds of data (whatever you determine as intelligence) to Elasticsearch and then display in the dashboards.

![Custom Feeds](http://1.bp.blogspot.com/-LD4fczfrQ8A/U43MO2W_GwI/AAAAAAAAAPo/U9Qq2t-x8kA/s1600/Screen+Shot+2014-06-03+at+3.23.03+PM.png)





