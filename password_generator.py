import random

def isInt(n):
    return not str(n).isdigit()


def getLength():
    dLen = 8
    print('Password length is: ' + str(dLen) + ' Press Enter to skip')
    while True:
        prompt = input('Enter Password length (must be at least 8): ')
        if prompt == '':
            return dLen
        elif isInt(prompt):
            print('Please enter a valid integer digit')
            continue
        elif int(prompt) < 8 or int(prompt) > 33:
            print('Password length has to be between 8 to 33')
            continue
        else: 
            dLen = prompt
            break

    return int(dLen)


def distributeLength(passwordLength):
    baseLength = passwordLength // 4
    extraLength = passwordLength % 4
    lengths = [baseLength] * 4
    lengths[random.randint(0, 3)] += extraLength

    return lengths



def choosePrimaryString(lengths):
    smallLetters = 'abcdefghijklmnopqrstuvwxyz'
    blockLetters = smallLetters.upper()
    specialCharacters = "!@#$%^&*?~"
    numbers = '1234567890'
    dataSet = [smallLetters, blockLetters, specialCharacters, numbers]

    return ''.join(
        ''.join(random.choice(dataSet[i]) for _ in range(lengths[i]))
        for i in range(4)
    )


def doPermutation(s):
    charList = list(s)
    random.shuffle(charList)

    return ''.join(charList)



def generateThePassword():
    defLen = getLength()
    lengths = distributeLength(defLen)
    primaryString = choosePrimaryString(lengths)

    return doPermutation(primaryString)


def regeneratePasswordOfSameLength(n):
    lengths = distributeLength(n)
    primaryString = choosePrimaryString(lengths)

    return doPermutation(primaryString)


def generateMultiplePasswords():
    passwords = int(input('How many passwords: '))
    length = int(input('Length of passwords: '))
    print('Here are your passwods: \n')
    for i in range(passwords):
        print(regeneratePasswordOfSameLength(length))


#! start of code...
if __name__ == '__main__':
    prompt = input('Do you want to 1] Generate multiple passwords of same length or 2] Generate single password: ').replace(' ', '')
    if prompt == '1':
        generateMultiplePasswords()
    else:
        password = generateThePassword()
        print('Your password is: ' + password)
        genereatedPasswordLength = len(password)
        while True:
            prompt = input('Press 1, 2, anything else to Regenerate password of same length, Generate password of new length, Quit respectively: ')
            if prompt == '1':
                password = regeneratePasswordOfSameLength(genereatedPasswordLength)
                print('Password regenerated: ' + password)
            elif prompt == '2':
                password = generateThePassword()
                print('Your password is: ' + password)
                genereatedPasswordLength = len(password)
            else: 
                break
    
    print('Program terminated!')
    
            


       

