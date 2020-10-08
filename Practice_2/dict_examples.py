# price = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
# print(price)
# stock={}
# #Add values
# stock["banana"]= 6
# stock["apple"]= 0
# stock["orange"] =32
# stock["pear"]= 15
# print(stock)

# for x in price:
#     print(x)
#     print('Price :',price[x])
# #     print('Stock :',stock[x])
#
# total = 0
# for y in price:
#     amt = price[y]*stock[y]
#     print('{0} : {1}'.format(y,amt))
#     total += amt
# print(total)

#Exercise 2
# groceries = ["banana","orange", "apple"]
# stock = {"banana": 6,"apple": 0,"orange": 32, "pear": 15}
# prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

##Question 1 :Define a function compute_bill that takes one argument food as input. In the function, create a variable total with an initial value of zero.For each item in the food list, add the price of that item to total. Finally, return the total. Ignore whether or not the item you're billing for is in stock.Note that your function should work for any food list.

# def compute_bill(food):
#     total = 0
#     for food in groceries:
#         if stock[food] > 0:
#             amt = prices[food]
#             print("{0} = {1}".format(food,amt))
#             total = total + amt
#             remaining_Stock = stock[food]-1
#     return total
#
# print('Total Bill :',compute_bill(groceries))

lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

lst = [lloyd,alice,tyler]

for i in lst:
    print (i)

def average(numbers):
    total = sum(numbers)
    total = float(total)
    ave = total / len(numbers)
    return ave

def get_average(student):
    homework = average(student['homework'])
    quizzes = average( student['quizzes'] )
    tests = average( student['tests'] )
    final = 0.1*homework + 0.2*quizzes + 0.3*tests
    return final

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "E"

#for i in lst:
    print(get_letter_grade( get_average(lloyd) ))

