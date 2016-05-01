from io import StringIO
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://amg.bktbp.com/monitor.php")
bsObj = BeautifulSoup(html, "html.parser")
ss = bsObj.script.get_text()

scrip_txt = StringIO(ss)

# def getmarks(script, initstring):
# 	for line in script:
# 		if line.startswith(initstring):
# 			elementos = line.split(",")
# 			for elemento in elementos:
# 				print(elemento+',')
#getmarks(scrip_txt, 'newMarker')

def getmarks(script, initstring):
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

			mark = {"status": status , "lat": float(lat) , "long": float(lon) , "id": idname , "station-desc": stationdesc , "total": int(totalcapacity) , "espacios": int(freespaces) , "bicicletas": int(bikes)}
			print(mark)

getmarks(scrip_txt, 'newMarker')


#experiment area
