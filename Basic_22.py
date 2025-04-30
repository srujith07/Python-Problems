str1 = "pynative.com is for python lovers"

ns = []
for i in str1.split():
    te = i[0].upper()+i[1:]
    ns.append(te)

for i in ns:
    print(i, end=" ")



