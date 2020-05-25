# Question 7: Return the total count of string “Parag” appears in the given string


def stringCount(statement):
    print('Given string count is', statement)
    count = 0
    for i in range(len(statement)-1):
        count += statement[i: i+4] == 'Parag'
    return count
count = stringCount('Parag is good Python coder ,Parag is good Automation Engineer')
print(count)