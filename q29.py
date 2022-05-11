l=[5,6,[],3,[],9]
b=[]
i=0
while i<len(l):
    if l[i]!=list():
        b.append(l[i])
    i+=1
print(b)
