# Question 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
thirdlist = []
print(listOne[:])
# for i in listOne:
#     if i % 2 != 0:
#         thirdlist.append(i)
# for i in listTwo:
#     if i % 2 == 0:
#         thirdlist.append(i)
# print(thirdlist)


# Exercise Question 2: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
speed  ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,
          'july':54, 'Aug':44, 'Sept':54}

speedlist =speed.values()
newlist = list(speedlist)
print(type(newlist))
print('Only Values :',speedlist)
print("Converted in list ",list(speedlist))
print("Converted in set: ",set(newlist))
# for i in speed.values():
#     print(i)
