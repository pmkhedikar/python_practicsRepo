#fetching the value one by one rather than load all the values
# Use the function to create generators
# saves the states of the local variables every time ‘yield’ pauses
# Python generators is more memory-efficient

def perfectSquare():
    n = 1
    while n <=10:
        sq = n **2
        yield sq
        n = n + 1
values = perfectSquare()

for i in values:
    print(i)