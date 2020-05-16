import  random

capitals ={'India':'Delhi', 'Bangladesh':'Dhaka' ,'Srilanka': 'Coloumbo' , 'Nepal' :'Katmandu' ,'Pakisthan':'Islamabad'}

for noOfPapers in range(3):
    quizQuestionfile= open(r"C:\Users\paragk1\PycharmProjects\SW_Python_Automation\automation_stuff\quiz\capitalQuiz%s.txt" % (noOfPapers+1) , "w")
    answereKeyFile = open(r"C:\Users\paragk1\PycharmProjects\SW_Python_Automation\automation_stuff\quiz\capitalQuiz_answeres%s.txt" % (noOfPapers+1), 'w')

#Write a header for Quiz
    quizQuestionfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizQuestionfile.write((''*20) + 'Contry Capitals Quize (Form%s)' % (noOfPapers+1))
    quizQuestionfile.write('\n\n\n')


    country = list(capitals.keys())
    random.shuffle(country)

for questionNum in range(5):
    correctAnswere = capitals[country[questionNum]]
    wrongAnswere = list(capitals.values())
    del wrongAnswere[wrongAnswere.index(correctAnswere)]
    wrongAnswere = random.sample(wrongAnswere,3)
    answereOption = wrongAnswere + [correctAnswere]
    random.shuffle(answereOption)


    for i in range(5):
        quizQuestionfile.write('%s. What is the capital of %s?\n' % (questionNum + 1, country[questionNum]))
        for i in range(4):
            quizQuestionfile.write('%s. %s\n' % (questionNum+1 , 'ABCD'[answereOption.index(correctAnswere)] ))
        quizQuestionfile.write('n')

        answereKeyFile.write('%s.%s\n' %(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizQuestionfile.close()
    answereKeyFile.close()