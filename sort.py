s=int(input("enter the size : "))
a=[]
for i in range(s):
    val=int(input("enter the number : "))
    a.append(val)
print("original list is : ",a)
for i in range(s):
    for j in range(0,s-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t     
print("sorted list is : ",a) 