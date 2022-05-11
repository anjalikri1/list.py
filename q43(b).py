l=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
i=0
k=3
l1=[]
while i<len(l):
    if i==k:
        l1.append("Z")
        k=k+3
    l1.append(l[i])
    i+=1
print(l1)

    