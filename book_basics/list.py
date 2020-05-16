# breakfast = ['eggs', 'milk', 'oats', 'tea']
# print(breakfast[1])
# print(breakfast[:])
# breakfast[1] = 'Toast'
# print(breakfast[:])
# print(len(breakfast[:]))
# del breakfast[2]
# print(breakfast[:])

#################################################
# catName =[]
# while True:
#     print("Enter the name of cat "+str(len(catName)+1) + 'Or enter nothing')
#     name = input()
#     if name == '':
#         break
#     catName = catName + [name]
# print('The list of cats is:')
# for names in catName:
#     print(names)

#################################################
# import random
# myPets =['tom','rocky','turbo','jully']
# print('enter the pet name')
# name = input()
# if name not in myPets:
#     myPets.append(name) #simply append add the end of list
#     myPets.insert(1,name) #specific to position
#     myPets.remove('rocky')
#     print('Sorry , I have not found ' + name +' in my pet list,we have added this in our list u get next time')
# else:
#     print("Got it")
#
# for name in (myPets):
#     print(name)
# print(myPets.sort(key=str.lower))
# print(myPets[random.randint(0, len(myPets)-1)])
# #################################################

list = ['Parag', 'Khedikar']
String = 'Parag'
Tupple = ('Parag', 1512, 'Talentica')

for i in String:
    print(i)

for i in list:
    print(i)

for i in Tupple:
    print(i)

bacon = [3.14, 'cat', 11, 'cat', True]

print(bacon.index('cat'))

print(bacon.append(99))