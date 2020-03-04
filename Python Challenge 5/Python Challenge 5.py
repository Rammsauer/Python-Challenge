import pickle

out = open("banner.p", "rb")
dict = pickle.load(out)
for line in dict:
    print("".join([k * v for k, v in line]))
out.close()
