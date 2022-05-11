l=[[1, 2, 4], [2, 4, 4], [1, 2]]
s1=0
s2=0
s3=0
i=0
a=[]
while i<len(l):
    j=0
    while j<len(l[i]):
        if j==0:
            s1+=l[i][j]
        elif j==1:
            s2+=l[i][j]
        else:
            s3+=l[i][j]
        j+=1
    i+=1
a.append(s1)
a.append(s2)
a.append(s3)
print(a)