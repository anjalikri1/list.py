l=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
k=4
l1=[]
while i<len(l):
    if i==k:
        l1.append(20)
        k=k+4
    l1.append(l[i])
    i+=1
print(l1)
    


