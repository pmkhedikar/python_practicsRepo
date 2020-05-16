def phoneNoValidtion(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
            return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# while True:
#     print('Plz enter 12 digit  phone no:')
#     phoneNo = input()
#     if phoneNoValidtion(phoneNo)==True:
#         print('Thanks for your phone no,Our representative will in touch with you')
#         break
#     else:
#         print('"'+ phoneNo +'"' + ' is invalid Phone No! Please try again')
# # print('Thanks for your phone no,Our representative will in touch with you')

message =("Sorry i am on vaccation ,please reach me on 111-222-3333 else call on my office no 123-123-12364")
print(len(message))
for i in range(len(message)):
    phoneNo =message[i:i+12]
    if phoneNoValidtion(phoneNo):
        print("Phone no found :" + phoneNo)
print('Thank you !')