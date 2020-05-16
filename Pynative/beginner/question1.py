#Question 1: Accept two integer numbers from a user and return their product and  if the product is greater than 1000, then return their sum

def twoNumber(a,b):
    if a*b>1000:
        return a+b
    else:
        return a*b

a = int(input('Enter first no : '))
b = int(input('Enter second no :'))
result = twoNumber(a,b)
print('Result of two no is :',result)