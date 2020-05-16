fruits =['Mango','Banana','Grapse']
veg =['tomato','potato','bringles']

for i in fruits:
    stringSize =0
    for length in i:
        stringSize= stringSize+1
    print("The {0} length is {1}".format(i,stringSize))

for index,fruits in enumerate(fruits):
    print(index)
    print(fruits)

i=0
length =len(veg)
print(length)
while i < length:
    print(veg[i])
    i=i+1

# for i in range(1,11):
#     for x in range(1,11):
# ############
# # isinstance(2,int)
# # isinstance(2.1,float)

# Elif Programm
    # print('Enter your age : ')
# age =int(input())
# if 18 < age < 25:
#     print('You are eligible for voting')
# elif age >= 25:
#     print('You are eligible for candidature')
# else:
#     print('Sorry you are not eligible')


# While Loop
    lst =[]
    n = int(input())
    i= 0
    while n >i:
        lst.append(input())
        i =i+1
    print(lst)
    mylist = list(set(lst))  # convert list to set to remove duplicates
    print(mylist)