# 49.
# Write a Python program to find the last occurrence of a specified item in a given list.
# Original list:
# ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
# Last occurrence of c in the said list:
# 15
# Last occurrence of k in the said list:
# 14
# Last occurrence of w in the said list:
# 12

# l=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# i=0
# while i<len(l):
#     if l[i]=="f":
#         a=i
#     i+=1

# # for i in range(len(l)):
# #     if l[i]=='f':
# #         a=i
# print(a)

    
l=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(l):
    if l[i]=="w":
        a=i
    i+=1
print(a)

