# Question 5: Given a list of numbers, return True if first and last number of a list is same

def first_and_last_Same(n):
    lst = []
    n = int(input('Enter list length:'))
    for i in range(0, n):
        inpuntNo = int(input())
        lst.append(inpuntNo)
    print('Given list is :', lst)
    if (lst[0] == lst[-1]):
        return True
    else:
        return False


print('Result is :', first_and_last_Same('Input'))
