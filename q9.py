l=[3,5,6,8,9,12,34,1,45,7]
max1=0
max2=0
max3=0
i=0
while i<len(l):
    if l[i]>max1:
        max1=l[i]
    i+=1
print(max1)
i=0
while i<len(l):
    if l[i]>max2 and l[i]!=max1:
        max2=l[i]
    i+=1
print(max2)
i=0
while i<len(l):
    if l[i]>max3 and l[i]!=max1 and l[i]!=max2:
        max3=l[i]
    i+=1
print(max3)


