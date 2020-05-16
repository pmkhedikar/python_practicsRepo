# details ={'name':'parag','surname':'khedikar'}
# print('My name is ',details['surname'])
#
#
####################################
# birthdays ={'parag':'15 dec','neha':'30 sept','mummy':'17 nov'}
#
# while True:
#     print("Enter your name :(Blank to quite)")
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(birthdays[name]+ " is the birthday of " + name)
#     else:
#         print('Sorry we have not found '+ name + ' in our database')
#         print('Kindly let us know the birthday')
#         bday=input()
#         birthdays[name]=bday
#         print('Database has updated')
#
####################################
# dic ={'name':'parag','company':'incedo'}
# for i in dic.keys():
#     print(i)
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic['company'])


###################################
import pprint
message = 'Hi this is parag khedikar and i am a moring person '
count ={}

for char in message:
    count.setdefault(char,0)
    count[char] = count[char] + 1
pprint.pprint(count)
