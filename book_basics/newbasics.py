import os

class AllInOne():
    path = r"C:\Users\paragk1\PycharmProjects\Practics_Stuff\automation_stuff"

    def countdir(self):
        countt = os.listdir(self.path)
        print(countt)
        print(len(countt))

    def countFiles(self):
        count = 0
        for i in os.listdir(self.path):
            if i.endswith('.py'):
                count= count + 1
        print(count)




a1 = AllInOne()
a1.countFiles()
a1.countdir()



