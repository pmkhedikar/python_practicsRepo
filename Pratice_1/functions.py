# # Given a string of odd length greater 7, return a string made of the middle three chars of a given String
#
# def getMiddleString(string):
#     a = 0
#     while a <= 0:
#         string = str(input('Enter any String:'))
#         if len(string) % 2 != 0:
#             middleindex = (len(string) // 2)
#             print(string[(middleindex - 1):(middleindex + 2)])
#             break
#         else:
#             print('Sorry! Please enter odd digit string value')
#             continue
#
# getMiddleString('a')




# # Print lower & upper case from string
# string = 'America known As UN'
# upper =[]
# lower =[]
# for i in string:
#     if i.islower():
#         lower.append(i)
#     else:
#         upper.append(i)
# lower.sort(reverse=False)
# upper.sort(reverse=False)
#
# print(''.join(lower))
# print(upper)




# # def String(a,b):
# #     if a in b:
# #         return True
# #     else:
# #         return False
# # print(String('en','eknabc'))
#
#
# #Find the string count in entire string
# string = "Parag is Tall , parag is Hadsome, isn't a Great "
# lst = string.split()
# count =0
# for i in lst:
#     if i =='Parag' or i =='parag':
#         count=count+1
# print(count)
# print(string.count('parag'))



# # Get the char count in string
# string = 'i am awesomee'
# countDir ={}
#
# for i in string:
#     #print(string.count(i))
#     count = string.count(i)
#     countDir[i]=count
# print(countDir)
