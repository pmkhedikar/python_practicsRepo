# str = 'Hi There'
# lst = list(str)
# length = len(str)
# newlist =[]
# for i in range(length):
#     newlist.append(lst[length-1-i])
# print(newlist)
# print(''.join(newlist))


n = str('153')
nlst = list(n)

def amstronNumber(n):
    length = int(len(nlst))
    summmation = int(nlst[0])**(length)+int(nlst[1])**(length)+int(nlst[2])**(length)
    if int(n) == summmation:
        print('{0} is Amstrong no '.format(n))
    else:
        print('Sorry')


amstronNumber(n)