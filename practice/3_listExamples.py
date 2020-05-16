# # 1.Print the list from inputs
#
# lst = []
# n = int(input('Enter any no : '))
#
# for i in range(0,n):
#     ele =int(input())
#     lst.append(ele)
# print(lst)


# 2. Try & catch - No max limit
# try:
#     my_list = []
#
#     while True:
#         ele = int(input())
#         my_list.append(ele)
# except:
#     print(my_list)


# 3. List of list
# lst =[]
# n = int(input('Enter Any number: '))
# for i in range(0,n):
#     ele = (input(),input(),int(input()))
#     lst.append(ele)
# print(lst)

# # 4. Get max no in List
# lst = []
# n = int(input('Enter any no:'))
#
# for i in range(0,n):
#     ele = int(input())
#     lst.append(ele)
# print(sorted(lst))
# print(max(lst))
# print(lst[-2])
# lst.remove(max(lst))
# print(max(lst))

# Covert list into Set to remove duplicates
lst =[]
n = int(input('Enter any number: '))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)

print(lst)
mylist = list(set(lst))   #Convert list into set
print(sorted(mylist))
print(mylist[-2])


