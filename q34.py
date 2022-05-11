l=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
a=[]
while i<len(l):
    if type(l[i])==int:
        a.append(l[i])
    i+=1
print(a)
