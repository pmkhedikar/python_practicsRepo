#sorting algorithm for numerical dataset

# lst = ['1','5','3','8']
# lst =[int(i) for i in lst]
# lst.sort()
# print(lst)
# #lst = map(int,lst)


## Find the value of A0,A1,A2....An
# A0 = dict(zip(('a,','b','c','d','d'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]

# print()
# p1 = [i for i in A0]   # Keys
# p2 = [A0[i] for i in A0] # Values
# print(p1 ,p2)
# p3 = {i:i**2 for i in range(1,11)} # Dict comprensive
# print(p3)
# p4 =[[i,i*i] for i in A1]  # List comprensive
# print(p4)

##########

# a= ['a','c','b','c','d','d']
# # b = []
# # for i in a :
# #     if i not in b:
# #         b.append(i)
# # print(b)
# b = list(dict.fromkeys(a))
# print(b)


### get length without using functions
# a = 'Parag'
# count = 0
# for i in a :
#     count = count + 1
# print(count)


stg = 'this is parag khedikar a python engineer'
stg1 = stg.split()
dict1 ={}

## length of each word in string
# for i in lst:
#     dict1[i]= len(i)
# print(dict1)

## count of each char in string
# for i in stg:
#     count = stg.count(i)
#     dict1[i] = count
# print(dict1)

# stg1.sort(key=len,reverse=True)
# newString = ' '.join(stg1)
# print(newString)
