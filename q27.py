# 27. Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]

a=int(input("enter the digit 1 :"))
b=int(input("enter the digit 2 :"))
c=int(input("enter the digit 3 :"))
d=[]
d.append(a)
d.append(b)
d.append(c)
print(d)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and j!=k and k!=i:
                print(d[i],d[j],d[k])
