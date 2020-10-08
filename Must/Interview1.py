## Print in reverse order
# str = 'This is forward string'
# lst = list(str)
# length = len(lst)
# newlist =[]
# for i in range(length):
#     newlist.append(lst[length-1-i])
# print(str[::-1])
# print(newlist)
# print(''.join(newlist))


## Armstrong Number
# n = str('153')
# nlst = list(n)
#
# def amstronNumber(n):
#     length = int(len(nlst))
#     summmation = int(nlst[0])**(length)+int(nlst[1])**(length)+int(nlst[2])**(length)
#     if int(n) == summmation:
#         print('{0} is Amstrong no '.format(n))
#     else:
#         print('Sorry')
#amstronNumber(n)


## Palindrome
# def palindrome(str):
#     s = set()
#     for i in range( len( str ) ):
#         expand( str, i, i, s )
#         expand( str, i, i + 1, s )
#     #print( s, end='' )
#     print( len( s ) )
#
# str = input()
# palindrome( str )


# Print lower & upper case from string
# string = 'America known As UN'
# #str = string.split()
# upper =[]
# lower =[]
# for i in string:
#     print(i)
#     if i.islower():
#         lower.append(i)
#     else:
#         upper.append(i)
# lower.sort(reverse=False)
# upper.sort(reverse=False)
# print(' '.join(lower))
# print(upper)



## Get the char count in string
# string = 'i am awesomee'
# countDir ={}
#
# for i in string:
#     #print(string.count(i))
#     count = string.count(i)
#     countDir[i]=count
# print(countDir)



## Leap Year
# def is_leap(year):
#     leap = False
#
#     if (year % 4 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         return True
#
#     if year % 4 == 0 and year % 100 == 0:
#         return False
#
#     return leap
#
# year = int(input())
# print(is_leap(year))


## String Sort by length
# string = 'My name is Parag and i am working in Talentica'
# print(list(string))  # it will convert each char in list
# lst = string.split()  # Convert string to List
# print(lst)
# lst.sort(key=len, reverse=True)  # Sorted list according to length & descending order
# print(lst)
# print(type(lst))
# SortedString = ' '.join(lst)  # Convert List to String
# print(SortedString)
# print(type(SortedString))




# dict1 = {'ename','eage','esal'}
# lst =[{'ename':'parag1','eage':'30','esal':'5000'},{'ename':'parag2','eage':'30','esal':'1000'},{'ename':'parag3','eage':'30','esal':'2000'}]
# lst.sort(key= lambda x : x['esal'],reverse=False)
# print(lst)



# stg = 'parag'
# dict1 = {}
# f = open(abc.txt,'r')
# readall = f.read()
# dict1 = {}
# for i in readall:
#     count = readall.count(i)
#     dict[i]= count
# print(count)


# def maximumOccurringCharacter(text):
#     dict1 = {}
#     for i in text:
#         count = text.count(i)
#         dict1[i] = count
#         sort_dict = sorted(dict1.items(),key= lambda x : x[1],reverse=True)
#     print( sort_dict )
#     lst1= sort_dict[0]
#     print(lst1[0])
# maximumOccurringCharacter('aabbbccdd')


# Find Max no in List
# n = [1,8,34,56,10,5]
# def MaxNumber(n):
#     maxNum = 0
#     for i in n:
#         if i > maxNum:
#             maxNum = i
#     print(maxNum)
# MaxNumber(n)
