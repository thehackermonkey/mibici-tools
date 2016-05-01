from io import StringIO
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime

html = urlopen("http://amg.bktbp.com/monitor.php")
bsObj = BeautifulSoup(html, "html.parser")
ss = bsObj.script.get_text()

scrip_txt = StringIO(ss)


#experiment area

def getmarks(script, initstring):
	date_handler = lambda obj: (
	obj.isoformat()
	if isinstance(obj, datetime.datetime)
	or isinstance(obj, datetime.date)
	else None
	)
	
	now = json.dumps(datetime.datetime.now(), default=date_handler)

	big_obj = {now: []}

	for line in script:
		if line.startswith(initstring):
			elementos = line.split(",")
			splitid = elementos[3].split(")")
			splitstatus = elementos[0].split("(")
			

			status = splitstatus[1].replace("'","")
			lat = elementos[1]
			lon = elementos[2]
			idname = splitid[0].replace("'(", "")
			stationdesc = splitid[1].replace("'(", "")
			totalcapacity = elementos[4]
			freespaces = elementos[5]

			bikesplit =elementos[6].split(")")
			bikes = bikesplit[0]


			result = {}
			result ["status"] = status
			result ["lat"] = float(lat)
			result ["long"] = float(lon)
			result ["station-desc"] = stationdesc
			result ["capacity"] = int(totalcapacity)
			result ["free-space"] = int(freespaces)
			result ["available-bikes"] = int(bikes)


			big_obj[now].append({str(idname): result})



	print(json.dumps(big_obj))

getmarks(scrip_txt, 'newMarker')