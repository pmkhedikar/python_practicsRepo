import os

path = os.path.join('user','bin','spam')
print(path)
myfiles =['abc.text','123.csv','newfile.smtp']
for i in myfiles:
    print(os.path.join('c:/filelocation/'+i))
print(os.getcwd())
print(os.path.split(os.getcwd()))
print(os.path.getsize(os.getcwd()))
print(os.getcwd())
totalsize =0
for i in os.listdir(r"C:\Users\paragk1\PycharmProjects\SW_Python_Automation\automation_stuff"):
    totalsize = totalsize + os.path.getsize(os.path.join(r"C:\Users\paragk1\PycharmProjects\SW_Python_Automation\automation_stuff" ,i))
    print(i)
print(totalsize)
print(os.path.exists(r"C:\Users\paragk1\PycharmProjectss"))
hellofile =open(r"C:\Users\paragk1\PycharmProjects\SW_Python_Automation\automation_stuff\6_String.py")
helloContent = hellofile.read()
print(helloContent)
newfile =open('newfile.txt', 'w')
newfile.write('Hello worldddddd\n')
newfile.close()
newfile = open('newfile.txt', 'a')
newfile.write('Second line in same file')
newfile.close()
newfile = open('newfile.txt')
newcontent = newfile.read()
print(newcontent)