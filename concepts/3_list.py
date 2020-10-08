# # Ordered Set of Objects
# # Allow Duplicates
# # Mutable
# # Surrounded by []
#
# familyMembers =['Vidya','Neha','Parag','Parag',1]
# print(familyMembers[2])
#
# #Two dimensional List
# Area = [['Baner','Aundha'],['Wagholi','Hinjewadi']]
# print(Area[0])
#
# #Add Element
# familyMembers.append('Gaatha')
# print(familyMembers)
#
# #Insert Element (Postion)
# familyMembers.insert(2,'Gaatha')
# print(familyMembers)
#
# #Delete Member
# familyMembers.remove(familyMembers[2])
# print(familyMembers)
#
# #Merge Two Lists
# familyMembers.extend(['Aai','Baba'])
# print(familyMembers)
#
# #Get Index
# get_index =familyMembers.index('Aai')
# print(get_index)
#
# #Remove the last item in list
# familyMembers.pop()
# print(familyMembers)
#
# # #Sort the list
# # print(familyMembers.sort())
#
# # Reverse the List
# print(familyMembers.reverse())

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


# def scrabble_score(word):
#     word = word.lower()
#     total_score=0
#     for i in word:
#         total_score= total_score +score[i]
#     return total_score
# print(scrabble_score('Abc'))


# def count(sequence,item):
#     count= 0
#     for i in sequence:
#         if i == item:
#             count += 1
#     return count
# print(count([2,3,4,5,5,6,7,5,55],5))


# def remove_duplicates(lst):
#     list1= []
#     for i in lst:
#         if i not in list1:
#             list1.append(i)
#     return list1
# print(remove_duplicates([1,2,3,1,23,2,3,23,23,5]))


################################ LIST COMPRENSION #################################
##Example 1:
# mylist_even = [i for i in range(0, 50) if i % 2 == 0]
# mylist_odd = [i for i in range(0, 50) if i % 2 != 0]
# print(mylist_odd)
#
# # def square(x):
# #     return x**2
# # lambda x :x**2
#
# mylist = range(0,16)
# print (filter(lambda x: x % 2==0,mylist))

##Example 2:
# cubes_by_four = [i**3 for i  in range(1,11)  if (i**3) % 4 ==0]
# print(cubes_by_four)

##Example 3:
# list1=[i for i in range(1,22)]
# print(list1)
# list1_odd = list1[0::2]
# print(list1_odd)
# middle_third = list1[7:14:1]
# print(middle_third)

# ##Example 4:
# list1_square=[i**2 for i in range(1,11)]
# list1_filter = print(list(filter(lambda x: x <= 70 and 30 <= x,list1_square)))

# s1 = input('enter S1 :')
# s2 = input('enter S2 :')

# def compare_string(s1, s2):
#     for i in  s1:
#         if i in s2:
#             return True
#         else:
#             return False
#
# print(compare_string(s1,s2))



#################find a particular data
string1 = "My name is Parag :32"
colon = string1.find(':')    #get the position of it
print(float(string1[colon+1:]))