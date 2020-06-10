my_tuple = ('parag',)
print(type(my_tuple))
print(my_tuple)

tuple_2 =('parag','khedikar',[15,12,1987],'parag')
print(type(tuple_2))
print(tuple_2[1][2])


name = ('parag')
lst=tuple(name)
print(type(lst))
print(lst)
for i in lst:
    print(type(i))
    print(lst.count(i))
