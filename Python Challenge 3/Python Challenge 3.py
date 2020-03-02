file1= open("python4.txt", "r")
read = file1.read()
z =0
k= 0
#

for i in read:
    if z == 3 and ord(read[k-4]) > 96 and ord(read[k-4]) < 123:
        if ord(i) > 96 and ord(i) < 123:
            if ord(read[k+1]) > 64 and ord(read[k+1]) < 91:
                if ord(read[k+2]) > 64 and ord(read[k+2]) < 91:
                    if ord(read[k+3]) > 64 and ord(read[k+3]) < 91:
                        if ord(read[k+4]) > 96 and ord(read[k+4]) < 123:
                            print(i)    #print(read[k-4],read[k-3],read[k-2],read[k-1],i, read[k+1],read[k+2],read[k+3],read[k+4])
                        else:
                            z = 0
                    else:
                        z = 0
                else:
                    z = 0
            else:
                z = 0
                
        else:
            z = 0          
    else:
        if ord(i) > 64 and ord(i) < 91:
            z = z+1
        else:
            z = 0
    k = k+1
