# Write a Python program to check if first digit/character of each element in a given list
# is same or not.

l=[1235,122,1984,19372,100]
i=0
b=str(l[0])[0]
count=0
while i<len(l):
    a=str(l[i])
    if a[0]==b:
        # print('true')
        count+=1
    # else:
        # print('false')
    i+=1
if count==len(l):
    print('True')
else:
    print('False')
        