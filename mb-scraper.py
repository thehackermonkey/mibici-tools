from io import StringIO
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://amg.bktbp.com/monitor.php")
bsObj = BeautifulSoup(html, "html.parser")
ss = bsObj.script.get_text()

scrip_txt = StringIO(ss)

def getmarks(script):
	for line in script:
		if line.startswith('newMarker'):
			print(line)


getmarks(scrip_txt)