class Parag():
    surname = 'Khedikar'

    def changeSurname(self, new_name):
        self.surname = new_name
        return new_name


objectNew = Parag()
print(objectNew.surname)
objectNew.changeSurname('new')
print(objectNew.surname)

