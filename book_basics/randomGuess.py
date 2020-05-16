import random

print("Let's Guess any no between 1 to 20 & get a Prize !!")
lucky_number =random.randint(1,20)
print(lucky_number)

for i in range(0,5):
    print("Please guess the number :")
    entered_no = int(input())
    if entered_no > lucky_number:
        print("Please guess bit low ")
    elif entered_no < lucky_number:
        print("Please guess bit high")
    else:
        break

if entered_no==lucky_number:
    print("Ohh you guess correctly")
else:
    print("Sorry ,You have cross the maximum limit")