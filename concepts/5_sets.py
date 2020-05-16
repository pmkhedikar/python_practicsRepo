# Unordered data
# Non-duplicates collection
# Mutable
# Surrounded by ()
# Any data type
# set() build in function

name = set('1Parag')
print(name)   #output will be in {}

furniture =set(['222dinning table','wardrobe','study table'])
print(furniture)

numbers = set(["3333apple",2,3,3,3,34,56,6,5,'mango'])
print(numbers)


#Add value in set
furniture.add('444bed') # add 1 argument
print(furniture)
furniture.update(('555mirror','comb')) #add multiple argument
print(furniture)

#Add tuple in set
numbers.add((99,88))
numbers.update((77,66))
print(numbers)


# Delet
numbers.discard(2)
print(numbers)

#Merge two sets
numbers1 =set([11,12,13,3,5])
print(numbers & numbers1)

#Concatination
a ={1,2,3,1,'abc'}
b ={3,4,5,'Parag','abc'}

print(a|b)
print(a.union(b))


# Intersection
print(a&b)
print(a.intersection(b))

# Difference
print(a-b)
print(b-a)

# Frozen set
d = frozenset(a)
print(d)