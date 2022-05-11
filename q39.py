# Write a Python program to compute the average of n th elements in a given list of
# lists with different lengths.
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]


l=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
while i<len(l):
    j=0
    s=0
    a=[]
    while j<len(l[i]):
        s=s+l[j][i]
        a.append(s)
        j+=1
    i+=1
print(a)


