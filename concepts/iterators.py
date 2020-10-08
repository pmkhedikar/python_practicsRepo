#Use iter() and next() functions.


class Topten():
    def __init__(self):
        self.num= 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

T = Topten()
for i in T:
    print(i)