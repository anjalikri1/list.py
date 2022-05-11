l=[["g","f","g"],["i","s"],["b","e","s","t"]]
i=0
a=""
while i<len(l):
    j=0
    while j<len(l[i]):
        a=a+l[i][j]
        j+=1
    i+=1
print(a)

