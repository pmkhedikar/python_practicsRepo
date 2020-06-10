def add(a,b=10):
    c =a+b
    return c

print(add(2))
print(add(2,3))


def multiplearg(*names):
    print(names)
multiplearg('parag','neha','Gatha','parag')

