# def foo(k):
#     k = [1]
# q = [0]
# foo(q)
# print(q)



# dictionary1 = {'google':1,'facebook':2,'MS':3}
# dictionary2 = {'yaaho':1 ,'MS':2,'youtube':3}
#
# dictionary1.update(dictionary2);
# print(dictionary1)
# for key, values in dictionary1.items():
#     print(key,values)



# value = [1, 2, 3, 4, 5]
# try:
#     value = value[5]/0
# except (IndexError, ZeroDivisionError):
#     print('Except', end ='')
# else:
#     print('Else', end ='')
# finally:
#     print('finally', end = '')


class A:
    def __init__(self):
        self.__i = 1
        self.j = 5

    def display(self):
        print(self.__i, self.j)

class B(A):
    def __init__(self):
        super().__init__()
        self.__i = 2
        self.j = 7

b = B()
b.display()

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
# def ordinary():
#     print("I am ordinary")
#
# pretty = make_pretty(ordinary)
# pretty()


# lst = [1,'a',5]
#
# for i in range(len(lst)):
#     try :
#         output = lst[i] % 2 == 0
#         print(output)
#     except:
#         print('exception is coming')
#
#     else:
#         print(lst[i])
#
#     # finally:
#     #     print('finally')


# n = [1,8,34,56,10,5]
# def MaxNumber(n):
#     maxNum = 0
#     for i in range(len(n)-1):
#         if n[i] > maxNum:
#             maxNum = n[i]
#     print(maxNum)
# MaxNumber(n)


# tuple = ('a','b','c')
# lst =list(tuple)
# print(''.join(lst))


# n = int(input('Enter any no: '))
# def evenOdd(n):
#     if n > 0:
#         if n % 2 == 0:
#             print('{0} is even no'.format(n))
#         else:
#             print('{0} is odd no'.format(n))
#     else:
#         print('Sorry you have entered negative no')
# print(evenOdd(n))


# for i in range(1,5):
#     for x in range(1,i+1):
#         print(x,end='')
#     print('')