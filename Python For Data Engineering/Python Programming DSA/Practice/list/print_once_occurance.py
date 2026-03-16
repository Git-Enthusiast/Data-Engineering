mystr = "a,a,a,b,b,c,c,c"
mystrlist = mystr.split(",")
mylist = []
for ele in mystrlist:
    if ele not in mylist:
        mylist.append(ele)
for ele in mylist:
    print(f"{ele}:{mystrlist.count(ele)}", end = ",")
    