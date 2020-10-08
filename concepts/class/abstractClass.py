# A method which have only declaration  & no defination  called abstractmethod
# And the class have  have abstractmethod is called abstract class
# By default Python not supporting abstractmethod
# Can't instantiate the abstract class having abstractmethod eg.#comp1 = Computer()
# it creates restriction to which method define

from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('Laptop class- Processing method')


#comp1 = Computer()
comp2 = Laptop()
comp2.process()