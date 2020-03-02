import time
from urllib import urlopen

surl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
si = "25357"
fs = urlopen(surl + si)
innertext = fs.read()
sn = ""

for n in innertext:
	if ord(n) > 47 and ord(n) < 58:
		sn = sn + n

for i in range(400):
	fn = urlopen(surl + sn)
	innertext = fn.read()
	sn = ""
	for n in innertext:
		if ord(n) > 47 and ord(n) < 58:
			sn = sn + n 
	print(surl + sn)
