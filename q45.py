l=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
i=0
a=[]
while i<len(l):
    if i<len(l)-3:
        a.append(l[i])
    i+=1
print(a)
