string = 'My name is Parag and i am working in Talentica'
#print(list(string))  # it will convert each char in list
lst = list(string.split())  # Convert string to List
print(lst)
lst.sort(key=len, reverse=True)  # Sorted list according to length & descending order
print(lst)
print(type(lst))
SortedString = ' '.join(lst)  # Convert List to String
print(SortedString)
print(type(SortedString))
