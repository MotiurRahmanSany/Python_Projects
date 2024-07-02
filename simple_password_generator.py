import random
import string


def generatePassword(n):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(random.sample(characters, n))


if __name__ == '__main__':
    print('Your password is: ' + generatePassword(int(input('Enter Length of passoword: '))))