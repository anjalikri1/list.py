# Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])


l= [[0], [1, 3], [5, 7],[9,3,4,6,9,11], [13, 15, 17]]
i=0
a=[]
while i<len(l):
    j=0
    c=0
    while j<len(l[i]):
        c+=1
        print(l[i]),
        # print("the list present in the index",i, "is",l[i])
        j+=1
    i+=1
# print(c)


