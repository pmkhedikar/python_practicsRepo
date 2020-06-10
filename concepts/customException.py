class Error(Exception):
    pass


class ValueTooSmall(Error):
    pass


class VlaueTooLarge(Error):
    pass


number = 10
while True:
    try:
        n = int(input('Guess the correct no :'))
        if n > number:
            raise VlaueTooLarge
        elif n < number:
            raise ValueTooSmall
        break
    except VlaueTooLarge:
        print('Dude its too large')
    except ValueTooSmall:
        print('Dude its too small')
print('Boom !! correctly guessed,You are Genius')
