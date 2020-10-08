# Lamda is anonymous function ,its used in inside another function.

# funName = lambda arguments : operation
# paa n no of argument with one line expression
# Example 1:
# a
# x = lambda a, b: a + b
# print(x(2, 3))
#
#
# # Example 2:
# def myfunc(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunc(2)
# print(mydoubler(11))

# MAP() ,FILTER() ,REDUCE()
from functools import reduce

# num = [1, 4, 7, 2, 9, 10, 24, 12, 3,10]
#
# even = list(filter(lambda n: n % 2 == 0, num))  #set to remove duplicates
# print(even)
#
# # The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
# squares = list(map(lambda n: n ** 2, even))
# print(squares)
#
# listSummation = list(map(lambda a, b: a + b, even, squares))
# print(listSummation)
#
# summation = (reduce(lambda a, b: a + b, squares))
# print(summation)


lst = [1,3,5,6,8]
a = list(filter(lambda x : x % 2 == 0, lst ))
print(a)
