l=[15, 81, 11, 234]
i=0
c=[]
while i<len(l):
    b=l[i]%10
    l[i]=l[i]//10
    c.append(b+l[i])
    i+=1
print(c)

