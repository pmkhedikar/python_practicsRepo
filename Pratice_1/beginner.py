# #Question 1: Accept two integer numbers from a user and return their product and  if the product is greater than 1000, then return their sum
#
# def twoNumber(a,b):
#     if a*b>1000:
#         return a+b
#     else:
#         return a*b
#
# a = int(input('Enter first no : '))
# b = int(input('Enter second no :'))
# result = twoNumber(a,b)
# print('Result of two no is :',result



# # Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
#
# print("Printing current and previous number sum in a given range(10)")
#
#
# def sumNum(num):
#     previousNum = 0
#     for i in range(num):
#         sum = previousNum + i
#         print('Current no is :{0} and previous no is :{1} and there summation is {2}'.format(i, previousNum, sum))
#         previousNum = i
# sumNum(10)



# # Question 3: Accept string from a user and display only those characters which are present at an even index number.
#
# def getEvenindex(inputsting):
#     inputString =str(input('Enter any string :'))
#     print('Printing only even index charaters')
#     for i in range(len(inputString)):
#         if i % 2 ==0:
#             print(inputString[i])
#         else:
#             continue
# getEvenindex('String')



# # Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
# def getString(inputstr):
#     InputSting = str(input('Enter any string: '))
#     InputInteger = int(input('Enter any no: '))
#     getStringLength = len(InputSting)
#     loopcount= getStringLength-InputInteger
#     for i in range(loopcount):
#         print(InputSting[InputInteger + i])
#         if InputInteger > getStringLength:
#             print('N should be less than length of string')
#             InputInteger = int(input('Enter any no: '))
#         else:
#             continue
# getString('abc')
#
# # Approach 2
# # def remoechar(str,n):
# #     return[n:]



# # Question 5: Given a list of numbers, return True if first and last number of a list is same
#
# def first_and_last_Same(n):
#     lst = []
#     n = int(input('Enter list length:'))
#     for i in range(0, n):
#         inpuntNo = int(input())
#         lst.append(inpuntNo)
#     print('Given list is :', lst)
#     if (lst[0] == lst[-1]):
#         return True
#     else:
#         return False
#
#
# print('Result is :', first_and_last_Same('Input'))



# # Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
#
# def divisibleByFive(lst):
#     print('Given list is: ',lst)
#     # print('No divisible to 5 are :')
#     for num in lst:
#         if num % 5 != 0:
#             print('{0} is not divisble to 5'.format(num))
#         else:
#             print('{0} is Divisible to 5'.format(num))
#
#
# GivenList = [6, 110, 23, 45, 68, 70]
# divisibleByFive(GivenList)



# # Question 7: Return the total count of string “Parag” appears in the given string
#
#
# def stringCount(statement):
#     print('Given string count is', statement)
#     count = 0
#     for i in range(len(statement)-1):
#         count += statement[i: i+4] == 'Parag'
#     return count
# count = stringCount('Parag is good Python coder ,Parag is good Automation Engineer')
# print(count)



# # Question 8: Print the patter
#
# for i in range(10):
#     for x in range(i):
#         print(i,end='')
#     print('')
