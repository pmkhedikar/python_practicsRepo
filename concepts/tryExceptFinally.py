import sys
import json
import functools
import array



# lst = [2, 5, 20, 0, 'a', 34, 45]

# for i in lst:
#     if i % 5 == 0:
#         print(i)
#     else:
#         print('Is no divisible to 5 :', i)

# for i in lst:
#     try:
#         if i % 5 == 0:
#             print(i)
#         else:
#             print('Is no divisible to 5 :', i)
#     except:
#         print('Got Error =', i, sys.exc_info()[0])


# for i in lst:
#     try:
#         if i % 5 ==0:
#             print('Perfectly divisible to 5',i)
#     except:
#         print('Opps! Got error =>', sys.exc_info()[0])




# randLst = ['a', 0, 2,3]
# for entry in randLst:
#     try:
#         print('The entry is :', entry)
#         div = 1 / int(entry)
#         break
#     except:
#         print('Exception -', sys.exc_info()[0])
#         print('Next Entry \n')
# print('The value of div is :', div)


##########################################################################
##Raise
# try:
#     n = int(input('Enter any no :'))
#     if n <=0:
#         raise ValueError('This is not Positive number')
# except ValueError as error:
#     print(error)
#
# print('Value of {0} square is : {1}'.format(n,n*n))


#Try ...else
# try :
#     n = int(input('Enter any no: '))
#     assert n % 2 == 0
# except:
#     print('{0} Not an even No'.format(n))
#
# else:
#     div =1/n
#     print(div)

## try .finally
# try:
#    f = open("test.txt",encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()