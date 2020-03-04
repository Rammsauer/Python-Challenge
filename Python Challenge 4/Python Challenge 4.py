from urllib.request import urlopen
import re

surl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
si = "96791"
fs = urlopen(surl + si)
innertext = fs.read()
sn = str(int(innertext.split()[5]))

for i in range(400):
	fn = urlopen(surl + sn)
	innertext = fn.read()
	sn = str(int(innertext.split()[5]))
	print(surl + sn)

#1. Hürde bei 94485
#2. Hürde bei 16044
#3. Hürde bei 82682
#peak.html
