# Unordered set of key & values
# Non Duplicates
# Surrounded by {}



familyProfession = {'Parag': 'Sr QA Engineer', 'Vidya': 'Social Worker', 'Neha': 'Buisness Analyst', 'City': 'Pune'}

print(familyProfession.keys())  # get list of keys
print(familyProfession.values())  # get list of values

print(familyProfession['Parag'])
print(familyProfession['City'])  # Get Value of Key
print(familyProfession.get('Pune'))  # Get method to get value of key

for k, v in familyProfession.items():  # Make dict callable
    print('Key is {0}'.format(k))
    print('Values is {0}'.format(v))
    print('\n', end='')

# Add Values in dictonary
familyProfession['Surname'] = 'Khedikar'
print(familyProfession)

#Merge  two directories
familyProfession_maternal = {'Aai': 'Housewife', 'Baba': 'Shopkeeper'}
familyProfession.update(familyProfession_maternal)
print(familyProfession)

# Delete dictonary values , Del is a KEY (It give exception error if value is not present)
del familyProfession['Surname']
print(familyProfession)

# Pop for delete (it returns None if vale not present)
familyProfession.pop('City')
print(familyProfession)
familyProfession.pop('City', None)  # None is default argument we have to pass

# Get the key present or not
# familyProfession.has_key('Parag')

# Get input in Dictonaries & convert dict to list
d ={}
n = int(input())
for i in range (0,n):
    name = str(input())
    score = float(input())
    d[name]=score
print(d)
print(list(d.items()))
print(list(d.keys()))
print(list(d.values()))

