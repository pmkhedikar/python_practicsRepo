# Ordered series of same data type
# Array Vs List - List can store different data types
# Array are mutable(Changeable)

import array as arr

a = arr.array('i',[1,2,3,4,5])
print(a)
print(a[1])

# length of an array
print(len(a))

# Adding elements in Array
# Append - To add element at the end of array
# Extend - To add multiple elements
# Insert - To add element in particular position

b = arr.array('d',[1.1,2.2,3.3])
print(b)
b.append(4.4)
print(b)
b.extend([5.5,6.6,7.7])
print(b)
b.insert(1,0.0)
print(b)

# remove element
# Pop - remove element & return
# remove() - remove without return

print(b.pop())
print(b.pop(2)) #return the value
print(b)
print(b.remove(5.5)) #Not return anything
print(b)