import random
from text_to_emoji import textToEmoji 

def isValidInput(prompt):
    judgeAns = ''
    if not prompt.isdigit():
        judgeAns = 'Please enter a valid quiz number in positive integer -> '
    elif prompt.isdigit() and int(prompt) < 5:
        judgeAns = 'Number of quizes has to be at least 5 -> ' 
    else: 
        judgeAns = 'okay'

    return judgeAns
    



def quizGame(quizes):
    score = 0
    correct = 0

    for i in range(quizes):
        print(textToEmoji('\nRemaining quizes >~< : ' + str(quizes - i - 1)))
        print('\nWhat is ', end = '')
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        ch = random.randint(1, 4)
        ans = 0
        if ch == 1:
            ans = a + b; ch = '+'
        elif ch == 2:
            ans = max(a, b) - min(a, b); ch = '-'
        elif ch == 3:
            ans = a * b; ch = 'x'
        else: ans = max(a, b) // min(a, b); ch = '/'


        print(max(a, b), ch, min(a, b), ' = ', end='')

        userAns = input().strip()
        while not userAns.isdigit():
            userAns = input().strip()

        userAns = int(userAns)

        result = ''
        if userAns == ans:
            score += 10
            result = 'Correct! :)'
            correct += 1
        else: 
            score -= 5
            result = 'Incorrect! :('
            print('Ans:', ans)

        print(textToEmoji(result +  ' Your current score: ' + str(score)))

    return score, correct
        


if __name__ == '__main__':
    quizes = input('How many quizes? -> ').strip()

    while True:
        judgeAns = isValidInput(quizes)
        if judgeAns == 'okay':
            break
        else:
            quizes = input(judgeAns).strip()

    quizes = int(quizes)

    score, correct = quizGame(quizes)
    accuracy = round((correct / quizes) * 100)

    print('\n\n') 
    result = '    Result   '
    print(result.center(30, '*'))
    print('Your total score is:', str(score), '\t\nCorrect:',correct,'\t\nIncorrect:', (quizes - correct), '\nAccuracy: ' + str(accuracy) , '%')

    print('\n')

    if accuracy >= 90:
        print(textToEmoji('You are awesome mathematician!! :) :)'))
    elif accuracy >= 80:
        print(textToEmoji('You are so genious :) :)'))
    elif accuracy >= 70:
        print(textToEmoji('You did very well :)'))
    else: 
        print(textToEmoji('I know you can do good :) ... keep trying.. don\'t loose hope >~<'))