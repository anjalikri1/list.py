l1=['0', '1', '2', '3', '4']
l2=['red', 'green', 'black', 'blue', 'white']
l3=['100', '200', '300', '400', '500']
i=0
a=[]
while i<len(l1):
    a.append(l1[i]+l2[i]+l3[i])
    i+=1
print(a)
    