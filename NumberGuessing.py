# Number Guessing #

import random

actual_val = random.randint(1,100)
attempts = []
attempt = 0

#def get_value():
    #val = int(input('Enter an integer between 1 and 100: '))
    #return val

def appending(number):
    global attempt
    attempt += 1
    attempts.append(number)
    return 0

#def net_score():
#    if (attempt > 0):
#        return int(score)

def starts():
    print('Currently you have 100 points, each wrong cause -10 points, so you have 10 attempts, if you wanna play, make a shot!')
    answer = input ("If you wanna guess number, then type 'Yes', otherwise 'No' please: ")
    score = 100
    print(actual_val)
    #print(score)
    #print(answer)
    while (answer == 'Yes'):
        print('Your current score: ', score)
        val = int(input('Enter an integer between 1 and 100: '))
        if (score > 0):
            appending(val)
            try:
                if int(val) < 1 or int(val) > 100:
                    raise ValueError("Please guess a number within the given range")

                if (val == actual_val):
                    print('Nicely done')
                    print('It took', len(attempts), 'tries!')
                    print('Overall entries:', *attempts)
                    print('Your net score is:', score)
                    break

                elif (val > actual_val):
                    print('Lower one needed')
                    score -= 10

                else:
                    print('Higher one needed')
                    score -= 10

            except ValueError as err:
                print("That is not a valid value. Try again!")
                print("({})".format(err))
        else:
            print('Nice try friend')
            break
    else:
        print('So long')
    return 0

starts()
