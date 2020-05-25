# Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number

print("Printing current and previous number sum in a given range(10)")


def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print('Current no is :{0} and previous no is :{1} and there summation is {2}'.format(i, previousNum, sum))
        previousNum = i


sumNum(10)
