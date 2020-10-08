# #Armstrong Number
# n = int(input('Enter the number: '))
# def armstrongNumber(n):
#     length = len(str(n))
#     list1 = list(str(n))
#     sum = 0
#     for i in range(length):
#         sum = int(list1[i])**(length) + sum    #convert the list into integer
#     print(sum)
#     if n == sum:
#         return True
#     else:
#         return False
# print(armstrongNumber(n))

# ##Reverse the list and
# list1 =[8,2,3,4,5,2,3,4,2,2,9,4]
# list1.sort()
# print(int(list1[]))

#str = input('Enter String :')
# str = 'this is parag and parag is tall'
# def checkCount(str):
#     lst = str.split()
#     for i in range(0, len(lst)):
#         count = 1
#         for j in range(i+1, len(lst)):
#             if (lst[i] == lst[j]):
#                 count += 1
#         if (count > 1 and lst[i] != "0"):
#             print(lst[i])
#
# checkCount(str)


# # Python program to find N largest
# lst = [1,22,3,45,6,55,8,25]
# n = 2
#
# def nMaxNumber(lst,n):
#     NewList = []
#     for i in range(n):
#         maxNum = 0
#         for j in range(len(lst)):
#             if lst[j] > maxNum:
#                 maxNum = lst[j]
#         lst.remove(maxNum)
#         NewList.append(maxNum)
#     print(NewList)
#
# nMaxNumber(lst,n)


## Python List Comprehension and Slicing
# lst = [1,4,7,88,2,3,4,99,100,13,18]
# odd_numbers = [ i**2  for i in range(1,10) if i % 2 != 0]
# odd_inList = [ i  for i in lst if i % 2 == 0]
# print(odd_numbers)
# print(odd_inList)
# odd,even = 0,0
# for x in range(len(lst)):
#     if x % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even,odd)


tuples = [(2),(),(5),(8),(5),()]

new_tuples = [i for i in tuples if (i)]
print(new_tuples)