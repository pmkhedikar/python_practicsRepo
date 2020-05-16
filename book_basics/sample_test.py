import random

capitals ={'India':'Delhi', 'Bangladesh':'Dhaka' ,'Srilanka': 'Coloumbo' , 'Nepal' :'Katmandu' ,'Pakisthan':'Islamabad'}

desh = list(capitals.keys())
rajdhani = list(capitals.values())
print(capitals[desh[1]])
print(capitals[desh[2]])

# print(rajdhani.index(Delhi))


random.shuffle(desh)

print(desh)
print(rajdhani)


for questionNum in range(5):
    correctAnswere = capitals[desh[questionNum]]
    print(correctAnswere)
    # wrongAnswere = list(capitals.values())
    # print(wrongAnswere)
    # del wrongAnswere[wrongAnswere.index(correctAnswere)]
    # print(wrongAnswere)
    # print(path.c)