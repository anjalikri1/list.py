from re import I


a=int(input("enter the number :"))
b=len(str(a))
i=b-1
while i>=0:
    c=a//(10**i)
    d=c*(10**i)
    a=a%(10**i)
    print(d,"+",end="")
    i=i-1