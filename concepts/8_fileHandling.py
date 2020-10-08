# with open(r"C:\Users\paragk1\PycharmProjects\Practics_Stuff\automation_stuff\book_basics\sample.txt", 'r') as file:
#     # for i in range(5):
#     #     f.write('this is {0} line\n'.format(i))
#     # f.close()
#     # if f.mode == 'r':
#     #      print(f.read())
#
#     lines = file.readlines()
#     print(lines, end='')
#     print(lines[3])

# filePath = r"C:\Users\paragk1\PycharmProjects\Practics_Stuff\automation_stuff\concepts\sample_1.py"
# try:
#     f = open(filePath,'w')
# finally:
#     f.close()
#
# with open(filePath,'w') as f: # No need to close file it automatically handle internally
#     f.write('add 1st line \n')
#     f.write('add second line \n')
#     f.write('add third line \n')
#     print(f.tell())   # current position in no of bytes
#     f.seek(0)         # Started the cursor at 0 position -start position
#     f.write('added new line\n')
#
#
# print(f.readline())


######################## File  handling #################################
f = open('Sample_data_file','r')
f1 = open('abc','w')
#f1 = open('abc','a')        #to append
f1.write('writing something...')    # writing and scrap the old data

# print(f.read()) # read the entire content in file
# print(f.readline()) # read the first line
# print(f.readline(4)) # print four characters

for data in f:
    f1.write(data)


f = open(sample.jpeg, 'rb')
f1 = open(sample_copy.jpeg, 'wb')

for i in f:
    f1.write(i)