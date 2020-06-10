# # Question2 : Addition of two numbers:
# a = int(input('a ='))
# b = int(input('b ='))
# def add(a,b):
#     return a+b
# print(add(a,b))


# # Question3 : Python Program to Find the Square Root
# n = int(input('Enter no for squareroot :'))
# def squareRoot(n):
#     return n**(1/2)
# output= squareRoot(n)
# print('Square root is {:.2f}'.format(output))


## Question4: Python Program to Calculate the Area of a Circle
# r = int(input('Enter radius of Triangle:'))
# def areaOfTriangle(r):
#     return (22/7)*r*r
# print(areaOfTriangle(r))


## Question6 : Python Program to Swap Two Variables
# a = int(input('a ='))
# b = int(input('b ='))
# # a = a+b
# # b = a-b
# # a = a-b
# c = a
# a = b
# b = c
# print(a)
# print(b)

## Question 7 : generate a rondom no
# import  random
# print(random.randint(1,10))


## Question 12: Python Program to Check Leap Year
# def is_leap(year):
#     leap = False
#
#     if (year % 4 == 0 and year % 100 != 0):
#         return True
#     # elif (year % 100 == 0 and year % 400!=0):
#     #     return False
#     # elif (year % 400 == 0):
#     #     return True
#     # else:
#         return False
#     return leap
# year = int(input())
# print(is_leap(year))


## Python Program to Find the Largest Among Three Numbers
# lst = []
# for i in range(5):
#     x = input()
#     lst.append(x)
# print(lst)
# print(max(lst))


## Python Program to Check Prime Number
# n = int(input('Enter any no :'))
# def primeNumber(n):
#     for x in range(2,n):
#         if n % x ==0:
#             print('{0} is NOT prime number'.format(n))
#             break
#     else:
#         print('{0} is prime number'.format(n))
#
# primeNumber(n)


## Get a list of prime no in range
# def primeList(a, b):
#     for x in range(a, b):
#         for i in range(2, x):
#             if x % i == 0:
#                 break
#         else:
#             print(x)
# print(primeList(4, 100))


##Python Program to Find the Factorial of a Number
# n = int(input('Enter no for fatorial: '))
# def factorial(n):
#     fact =1
#     for i in range(1,n+1):
#         fact = fact *i
#     return fact
# print(factorial(n))


## Python Program to Display the multiplication Table from 1 to 10
# for i in range(1,11):
#     for n in range(1,11):
#         print(i * n)
#     print('\n')


##Python Program to Print the Fibonacci sequence
# n = int(input('Enter no for fab series: '))
#
# def fabSeries(n):
#     Num1 = 0
#     Num2 = 1
#     print(Num1,Num2,sep='/n')
#     for i in range(n + 1):
#         Sum = Num1 + Num2
#         Num1 = Num2
#         Num2 = Sum
#         print(Sum)
#
# fabSeries(n)


# ## Python Program to Display the multiplication Table
# n = int(input())
# def multiplication(n):
#     for x in range(1,n+1):
#         for i in range(1,11):
#             print('{0} X {1} = {2}'.format(x,i,x*i))
#         print('#'*20)
#
# multiplication(n)


# ## Find Armstronge Number:
# n = input('Enter Armstronge Number :')
# def armStrongNo(n):
#     lengthN = len(n)  # find the length of string ,int doesn't have length
#     lst =list(n)  #convert string to list but list is str type
#     print(lst)
#     print(type(int(lst[1])))
#     summ = 0
#     for i in range(lengthN):
#         x = int(lst[i])
#         summ = summ + (x**lengthN)
#     print(summ)
#     if summ == int(n):
#         print('{0} is armstrong number'.format(n))
#     else:
#         print('{0} is NOT armstrong number'.format(n))
#
# armStrongNo(n)


## Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# dec = int(input('Enter decimal number : '))
# print('Binary no is : {0} & its address is {1}'.format(bin(dec),id(dec)))
# print('Octal no is : {0} & its address is {1}'.format(oct(dec),id(dec)))
# print('Hexadeciamal no is : {0} & its address is {1}'.format(hex(dec),id(dec)))


##Python Program to Find ASCII Value of Character
# print(ord('p'))   # string conversation to ASCII value

## Find the absolute cube root
# def cubeRoot(n):
#     x = 1
#     while x > 0:
#         n = int(input('Enter no for cube root: '))
#         a = n ** (1 / 3)
#         if n % a == 0:
#             print('{0} is absolute cuberoot of {1}'.format(n,int(a)))
#             print('Great !')
#             break
#         else:
#             print('{0} is Not absolute cuberoot ! Value is {1}'.format(n,round(a,2)))
#             print('Plz try again !')
#             continue
# cubeRoot('n')


## find the factors of number
# n = int(input('Enter no of factor:'))
# def factor(n):
#     for i in range(1,n+1):
#         if n%i ==0:
#             print(i)
#         else:
#             continue
# factor(n)


##Python Program to Shuffle Deck of Cards
# import random
# lst = ['Heart','Diamond','Spread','Club']
# for i in range(5):
#     deck = random.randint(1, 14)
#     number = random.choice(lst)
#     print(deck,number)


## Python Program to Display Calendar
# import calendar
# yy = 2020
#
# for i in range(1,13):
#     print(calendar.month(yy ,i))


## Python Program to Display Fibonacci Sequence Using Recursion
# def fabRecur():
#     n = int(input())
#     n1 = 0
#     n2 = 1
#     for i in range(n):
#         sum = n1 + n2
#         n1 = n2
#         n2 = sum
#         print(sum)
# fabRecur()


## Python program to find the sum of natural using recursive function
# def rec_fab(n):
#     if n <= 1:
#         return n
#     else:
#         return n + rec_fab(n-1)
# print(rec_fab(10))


##String is Palindrome or Not
# my_str = 'paaraap'
#
# # make it suitable for caseless comparison
# my_str = my_str.casefold()
# rev_str = my_str[::-1] #reversed(my_str)
# print(rev_str)
# if my_str == rev_str:
#     print(True)
# else:
#     print(False)


## Python Program to Remove Punctuations/numerics From a String
#
# string = 'Hi this 123 is Parga ! @ do you love me ? 1'
# newString =[]
# for i in string:
#     if i.isnumeric() == True:
#         pass
#     else:
#         newString.append(i)
# print(''.join(newString))


# ## Python Program to Sort Words in Alphabetic Order
#
# word = 'zwxyzapple'
# word = list(word)
# word.sort()
# print(word)
# print(''.join(word))
#
# string ="This is string which gona be sort alphabetically"
# new = string.split()
# new.sort()
# print(new)
# print(' '.join(new))


# # Program to perform different set operations like in mathematics
#
# E = {0, 2, 4, 6, 8};
# N = {1, 2, 3, 4, 5};
# print("Union of E and N is",E | N)
# print("Intersection of E and N is",E & N)
# print("Difference of E and N is",E - N)
# print("Symmetric difference of E and N is",E ^ N)


# Program to total count the number of vowels in string
# Program to count the number of each vowels

vowels = 'aeiou'
string = 'Hello, have you tried our tutorial section yet?'


# Example =1
# count =0
# for i in list(string):
#     if i in vowels:
#         count = count+1
# print('Total no of volues in string is :',count)

# Example =2
# newString = list(string)
# countdir = {}
# for i in newString:
#     count = newString.count(i)
#     countdir[i] = count
# print(countdir)
# for key, value in countdir.items():
#     if key in vowels:
#         print(key,value)

## Python Program to Find the Size (Resolution) of a Image
def jpeg_res(filename):
    """"This function prints the resolution of the jpeg image file passed into it"""

    # open image for reading in binary mode
    with open(filename, 'rb') as img_file:
        # height of image (in 2 bytes) is at 164th position
        img_file.seek(163)

        # read the 2 bytes
        a = img_file.read(2)

        # calculate height
        height = (a[0] << 8) + a[1]

        # next 2 bytes is width
        a = img_file.read(2)

        # calculate width
        width = (a[0] << 8) + a[1]

    print("The resolution of the image is", width, "x", height)


jpeg_res("img1.jpg")
