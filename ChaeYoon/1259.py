mylist=[]
while True:
    val=input()
    if val=="0":
        break
    else:
        mylist.append(val)

result=[]

for val in mylist:
    if val==val[::-1]:
        result.append("yes")
    else:
        result.append("no")

for val in result:
    print(val)