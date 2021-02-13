# Rock Paper Scissors #

import random
import re

all = ['R','P','S']
answer = 'yes'
comp = 0
cand = 0

'''class ref:
    def __init__(self):
        self.variable = ['Original']
        self.Change(self.variable)
    def Change(self, var):
        var[0] = 'Changed' '''

def rand_generator():
    return random.choice(all)

def win(num):
    num += 1
    return num

def lose(val):
    val += 1
    return val

print("Welcome!")
while (answer == 'yes'):
    #score_win = 0
    #score_lose = 0
    response = input ("Choose one of three: Rock --> R, Paper ---> P, Scissors ---> S: ")
    component = rand_generator()
    print(component)
    if re.search(response, component, re.IGNORECASE):
        print("noice !")
        cand = win(cand)
        #print(cand)
    else:
        print("cry more !")
        comp = lose(comp)
        #print(comp)

    cont = input("Wanna continue? Yes or No: ")
    answer = cont.lower()
    #print(answer)

else:
    if (cand > comp):
        print("you win")
    elif (comp == cand):
        print("draw")
    else:
        print("you lost")
