#48. Write a Python program to split a given list into specified sized chunks.
l=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
b=[]
while i<=len(l)-3:
    b.append(l[i:i+3])
    i+=3
print(b)


