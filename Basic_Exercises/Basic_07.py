str_x = "Emma is good developer or developer. Emma is a writer"

lis = []

wrd = ""

chkd = []

for i in str_x:
    if i == " ":
        lis.append(wrd)
        wrd = ""
    if i != " " and i != ".":
        wrd = wrd+i

for i in lis:
    if i not in chkd:
        chkd.append(i)


cnts = []
for i in chkd:
    c =  0
    for j in lis:
        if i == j:
            c = c+1
    cnts.append(c)
#    print(i , c)

print(chkd)
print(cnts)

mx_cnts = []
mx_ind = 0
for i in cnts:

    if i is max(cnts):
        mx_cnts.append(mx_ind)
    mx_ind += 1
print(mx_cnts)

for i in mx_cnts:
    print("word","'"+chkd[i]+"'","occured",cnts[i],"Times")
