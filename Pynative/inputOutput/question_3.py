# Exercise Question 4: Display float number with 2 decimal places using print()
def add():
    a = float(input())
    b = float(input())
    return a+b


print("Values: ", add().__format__('.2f'))
