l=["a","b","c","d","e","f","g","h"]
i=3
a=[]
while i<len(l):
    a.append(l[i])
    i+=1
print(a)
j=1
while j<len(l):
    a.append(l[j])
    if j==2:
        break
    j+=1
print(a)
