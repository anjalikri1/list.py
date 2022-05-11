l=[1,2,2,5,8,4,4,8]
i=0
a=[]
while i<len(l):
    if l[i] not in a:
        a.append(l[i])
    i+=1
print(a)