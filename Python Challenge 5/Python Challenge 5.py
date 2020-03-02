import pickle
f = open("banner.p", "rb")
i = pickle.load(f)
for n in i:
    print(n)
#print(i)
