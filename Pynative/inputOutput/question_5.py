# Exercise Question 5: Accept list of 5 float numbers as a input from user
from typing import List


def acceptfloatValue():
    lst = []
    for i in range(5):
        lst.append(float(input()))
    return lst

print('List is :',acceptfloatValue())
