# Unordered set of key & values
# Non Duplicates
# Surrounded by {}

#
#
# familyProfession = {'Parag': 'Sr QA Engineer', 'Vidya': 'Social Worker', 'Neha': 'Buisness Analyst', 'City': 'Pune'}
#
# print(familyProfession.keys())  # get list of keys
# print(familyProfession.values())  # get list of values
#
# print(familyProfession['Parag'])
# print(familyProfession['City'])  # Get Value of Key
# print(familyProfession.get('Pune'))  # Get method to get value of key
#
# for k, v in familyProfession.items():  # Make dict callable
#     print('Key is {0}'.format(k))
#     print('Values is {0}'.format(v))
#     print('\n', end='')
#
# # Add Values in dictonary
# familyProfession['Surname'] = 'Khedikar'
# print(familyProfession)
#
# #Merge  two directories
# familyProfession_maternal = {'Aai': 'Housewife', 'Baba': 'Shopkeeper'}
# familyProfession.update(familyProfession_maternal)
# print(familyProfession)
#
# # Delete dictonary values , Del is a KEY (It give exception error if value is not present)
# del familyProfession['Surname']
# print(familyProfession)
#
# # Pop for delete (it returns None if vaule not present)
# familyProfession.pop('City')
# print(familyProfession)
# familyProfession.pop('City', None)  # None is default argument we have to pass
#
# # Get the key present or not
# # familyProfession.has_key('Parag')
#
# # Get input in Dictionaries & convert dict to list
# d ={}
# n = int(input())
# for i in range (0,n):
#     name = str(input())
#     score = float(input())
#     d[name]=score
# print(d)
# print(list(d.items()))
# print(list(d.keys()))
# print(list(d.values()))

################################## PRACTICE PROGRAMMING #################################
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# .sort()the items in the list stored under the 'backpack' key.
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key
# Add new key & value in inventory
# Remove the existing key & Value from directory
#
print(inventory)
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory['backpack'].sort())
# inventory['backpack'].remove('dagger')
# print(inventory)
# inventory['gold'] = inventory['gold']+50
# print(inventory)

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
#     name = input('Enter the Name :')
#     if name == '':
#         break
#     if name in birthdays.keys():
#         print(birthdays[name] + ' is birthday on ' + name)
#     else:
#         print('Sorry no entry found in database')
#         break
# for values in birthdays.items():
#     print(values)
# name = 'this is parag khedikar'
# count = {}

# for i in name:
# #     count.setdefault(i,0)
# #     count[i] = count[i] + 1
# # print(count)