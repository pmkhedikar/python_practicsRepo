import re
print('Please enter your no')
cutomerNo =input()
PhoneNumberRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
getNumberByFindall =PhoneNumberRegEx.findall(cutomerNo)
getNumber =PhoneNumberRegEx.search(cutomerNo)
print('Thanks for giving your phone no, Our support staff will call you on '+ getNumber.group())

message=input()
batRegEx = re.compile(r'Bat(wo)?man')
getText = batRegEx.search(message)
print('We get the text'+ getText.group())