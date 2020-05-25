# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def divisibleByFive(lst):
    print('Given list is: ',lst)
    # print('No divisible to 5 are :')
    for num in lst:
        if num % 5 != 0:
            print('{0} is not divisble to 5'.format(num))
        else:
            print('{0} is Divisible to 5'.format(num))


GivenList = [6, 110, 23, 45, 68, 70]
divisibleByFive(GivenList)
