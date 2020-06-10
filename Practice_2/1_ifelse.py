# # If & elif & else
# n = int(input())
# if n % 2 != 0:
#     print('Weird')
#
# elif n%2 == 0 and 2<=n<=5:
#     print('Not Weird')
#
# elif n%2 ==0 and 6<=n<=20:
#     print('Weird')
#
# else:
#     print('Not Weird')



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