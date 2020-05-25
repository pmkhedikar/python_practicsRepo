# Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
def getString(inputstr):
    InputSting = str(input('Enter any string: '))
    InputInteger = int(input('Enter any no: '))
    getStringLength = len(InputSting)
    loopcount= getStringLength-InputInteger
    for i in range(loopcount):
        print(InputSting[InputInteger + i])
        if InputInteger > getStringLength:
            print('N should be less than length of string')
            InputInteger = int(input('Enter any no: '))
        else:
            continue
getString('abc')

# Approach 2
# def remoechar(str,n):
#     return[n:]