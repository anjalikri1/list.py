# l=["floor","cheese","carrots"]
# i=0
# while i<len(l):
#     print(l[i])
#     i=i+1

number=[1,9,2,3,10,5,6,13]
i=0
a=number[0]
list=[]
while (i<len(number)):
    b=number[i]
    if b>a:
        # list.append(a)
        a=b
        # list.append(a)
    i+=1
    list.append(a)
print(list) 
