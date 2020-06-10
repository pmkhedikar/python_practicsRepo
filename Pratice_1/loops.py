# # Exercise Question 1: Print First 10 natural numbers using while loop
# n = 0
# while n < 10:
#     print(n)
#     n = n + 1



# # Exercise Question 2: Print the following pattern
# for i in range(1,6):
#     for n in range(i):
#         print(n+1, end='')
#     print(' ')



# # Exercise Question 3: Accept n number from user and calculate the sum of all number between 1 and n including n
# def factorial(n):
#     n = int(input('Enter the no for factorial: '))
#     summation = 0
#     for numbers in range(n+1):
#         summation = summation + numbers
#     return summation
# print('Summation is :',factorial('abc'))



# # Exercise Question 4: Accept n number from user and print its multiplication table
# def multiplicationNumber(n):
#     n = int(input('Enter the no for Multiplication: '))
#     for i in range(11):
#         print(n*i)
# multiplicationNumber('abc')



# # Exercise Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
#
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
# for x in range(len(list1)):
#     if (list1[x] % 5 == 0) and (list1[x] <= 150):
#         print(list1[x])
#     else:
#         continue



# # Exercise Question 6: Given a number count the total number of digits in a number
#
# n = input('Enter any no :')
# count = 0
# for i in n:
#     count += 1
# print('Total digits are: ',count)



# # Exercise Question 7: Print the following pattern using for loop
# x, y = 5, 5
# for n in range(0, x + 1):
#     for p in range(y-n,0,-1):
#         print(p, end='')
#     print('')



# # Exercise Question 8: Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]
# # n = len(list1)
# # for i in range(1,n+1):
# #     print(list1[n-i])
#
# for i in list1[::-1]:
#     print(i)



# # Exercise Question 9: Display -10 to -1 using for loop
# for i in range(-10,0,1):
#     print(i)
#
# #Exercise Question 10: Display a message “Done” after successful execution of for loop
# for i in range(5):
#     print(i)
# print("Done!")