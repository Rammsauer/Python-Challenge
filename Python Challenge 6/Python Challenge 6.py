import zipfile, re

sn = '90052.txt'
f = zipfile.ZipFile("channel.zip")
com = []
for i in range(910):
    try:
        n = f.read(sn).decode("utf-8")
        com.append(f.getinfo(sn).comment.decode("utf-8"))
        sn = str(n.split()[3]) + '.txt'
    except IndexError:
        continue

print("".join(com))

#Collect the Comments