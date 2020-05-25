# Question 3: Accept string from a user and display only those characters which are present at an even index number.

def getEvenindex(inputsting):
    inputString =str(input('Enter any string :'))
    print('Printing only even index charaters')
    for i in range(len(inputString)):
        if i % 2 ==0:
            print(inputString[i])
        else:
            continue
getEvenindex('String')

