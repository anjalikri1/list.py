check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]

check2[0] = 'Code'
check3[1] = 'Mcq'
count = 0
for c in (check1, check2, check3):
     print(c)
     if c[0] =='Code':
          count += 1
     if c[1] =='Mcq':
          count += 10
print(count)






# l1=[2,4,5,6]
# l2=["anjali","sonam",3,5,6]
# l3=["abc",3,5,6,7]
# c=0
# for i in (l1,l2,l3):
#     if i[0]==2:
#         c+=1
#     if i[1]=="sonam":
#         c+=10
# print(c)