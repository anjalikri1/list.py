l = [2, -7, 5, -64, -14]
i=0
c1=0
c2=0
while i<len(l):
    if l[i]>0:
        c1+=1
    elif l[i]<0:
        c2+=1
    i+=1
print("negative no:",c2)
print("negative no :",c1)

