import json
from datetime import date
try:
    import urllib.request as urllib2
except ImportError:
	import urllib2

id = "16412458"       #ID da medicao
url = "https://atlas.ripe.net/api/v2/measurements/" + id + "/results/?format=json"
data = urllib2.urlopen(url)
data = json.load(data)

probes = int(len(data))  # Quantidade de probes 

i = 0
for i in range(probes):
	print (str("Probe ID: ")  + str(data[i]['prb_id'])) 	# PROBE ID
	
	print (str("Result "))
	for result  in data[i]['result']:
		try:
			print( "	RTT " + str(result['rtt']) )
		except:
			print ("	RTT " + str(result) + "x ") 


	print(str("____--___--____--____--____"))
	print(" ")

