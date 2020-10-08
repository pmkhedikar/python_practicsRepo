dict1 = {'ename','eage','esal'}
lst =[{'ename':'parag1','eage':'30','esal':'5000'},{'ename':'parag2','eage':'30','esal':'1000'},{'ename':'parag3','eage':'30','esal':'2000'}]
lst.sort(key= lambda x : x['esal'],reverse=False)
print(lst)



stg = 'parag'
dict1 = {}
f = open(abc.txt,'r')
readall = f.read()
dict1 = {}
for i in readall:
    count = readall.count(i)
    dict[i]= count
print(count)


def maximumOccurringCharacter(text):
    dict1 = {}
    for i in text:
        count = text.count(i)
        dict1[i] = count
        sort_dict = sorted(dict1.items(),key= lambda x : x[1],reverse=True)
    print( sort_dict )
    lst1= sort_dict[0]
    print(lst1[0])
maximumOccurringCharacter('aabbbccdd')


##Ip address:
import re

number = int(input())

for n in range(number):
    string = input()
    if re.search(r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$', string):
        print('IPv6')
    elif re.search(r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', string):
        print('IPv4')
    else:
        print('Neither')
        