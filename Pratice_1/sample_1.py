# n = int(input())
# dict ={}
# for i in range(0,n):
#     studentInput = map(str,int,input(),input())
#     dict[studentInput]
# print(dict)
#


# d = {}
# n = int(input())
# for i in range (0,n):
#     name = str(input())
#     score = float(input())
#     d[name]
#     d[score]
# print(d)

# d ={}
# n = int(input())
# for i in range (0,n):
#     name = str(input())
#     score = float(input())
#     d[name]=score
# d =[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
d = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41, 'Harsh': 39}
# print(d)
# print(list(d.items()))
# Key_list =(list(d.keys()))
# Value_List = list(d.values())
# Value_scoreOrderedList = list(sorted(Value_List))
# print(Value_scoreOrderedList)
# print(Key_list[Value_List.index(70)])
# print(Key_list[Value_List.index(Value_scoreOrderedList[0])])
# print(Key_list[Value_List.index(Value_scoreOrderedList[1])])
# print(d)
# studentNames = list(d.keys())
# studentScores = list(d.values())
# sortedScore = list(sorted(studentScores))
# print(sortedScore)
# print(sortedScore[0])
# print(studentNames[studentScores.index(sortedScore[0])])
# print(studentNames[studentScores.index(sortedScore[1])])
# print(studentNames[studentScores.index(sortedScore[2])])


# lst=[['neha', 11.0], ['parag23', 22.0],['mummy',6.0],['gaatha',22.0],['gaatha',222.0]]
#
# # n =int(input())
# # for i in range(0,n):
# #     name=str(input())
# #     score=float(input())
# #     lst.append([name,score])
# print(lst)
# print(sorted(lst))
# print(sorted(lst[0:1],reverse=False))

# d= {}
# for _ in range(input()):
#     name= str(input())
#     marks =float(input())
#     d[name]=marks
# print(d)


# for i in range(0,5):
#     print(i)
#     if i < 2:
#         print('Executing if loop')
#     else:
#         print('else loop')
#         pass


# values =('parag',1,2,3,1,'parag','neha')
# for x in values:
#     print(x)
# str1,str2,str3 =input('Enter the string :').split()
# print(str1,str2,str3)
#
# quantity = 3
# totalMoney = 1000
# price = 450
# print('i have {0} quantities of {1} price so that total money is {2:.2f}'.format(quantity,price,totalMoney))

# def fatorial(n):
#     multi =1
#     for i in range(1,n+1):
#         multi= multi*i
#     return multi
# print(fatorial(11))

# a = 'i work in pubmatic'
# lst = list(a.split(' '))
# print(lst)
# for i in lst:
#
# lst = [1, 10, 15, 34, 30, 100, 65, 180, 22]
# even = []
# odd = []
# for i in range(len(lst)):
#     if (lst[i] % 2 == 0) and (lst[i] <=100):
#         even.append(lst[i])
#     elif(lst[i] %2 != 0):
#         odd.append(lst[i])
#     else:
#         print(lst[i])
# print('Even :',sorted(even,reverse=True))
# print('Odd :',sorted(odd))


lst = [1,2,3,4,5,6]
print(lst[::-1])