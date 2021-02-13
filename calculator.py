# CALCULATOR (summation, substraction, multiplication, division for now)
# couldn't make it dynamic :(
import re
import itertools

'''def check(comings):
    if('*' in comings):
        return comings.partition("*")
    elif('/' in comings):
        return comings.partition("/")
    elif('+' in comings):
        return comings.partition("+")
    elif('-' in comings):
        return comings.partition("-")
    else:
        print("Not valid!!!")
        return 0


def calculate():
    operation = input("Enter the calculation you want to make, without spaces: ")
    operation = operation.rstrip()
    print(operation)
    # letters.split('*')[0]
    parts = check(operation)
    print(parts)
    former = parts[0]
    latter = parts[2]'''


def addition():
    num = input("Enter the first value: ")
    sum = 0
    total = 0
    while num != '00':
        sum = sum + float(num)
        num = input("Enter the value (00 for quit) ")
        total = total + 1
    else:
        return sum


def subs():
    num1 = input("Enter the first value: ")
    diff = 0
    total = 0
    holder = 0
    num = 0
    while str(num) != '00':
        num = input("Enter the value (00 for quit) ")
        if holder == 0:
            diff = float(num1) - float(num)
            holder += 1
        else:
            diff -= float(num)
        total = total + 1
    else:
        return diff

def multiplication():
    num = input("Enter the first value: ")
    mul = 1
    total = 0
    while num != '00':
        mul = mul * float(num)
        num = input("Enter the value (00 for quit) ")
        total += 1
    else:
        return mul

def division():
    num1 = input("Enter the first value: ")
    div = 0
    total = 0
    holder = 0
    num = 1
    while str(num) != 'q':
        if holder == 0 and float(num) != 0 :
            div = float(num1) / float(num)
            holder += 1
            num = input("Enter the value (q for quit) ")
        elif holder != 0 and float(num) != 0 :
            div /= float(num)
            num = input("Enter the value (q for quit) ")
        elif float(num) == 0:
            print("Miss entrance")
            break
        total = total + 1
    else:
        return div


while True:
    op = input("Enter the operation you want to realize: + , - , * , / or q(quit) ")
    if op != 'q':
        if(op == '+'):
            print("Result is ", addition())
        elif(op == '-'):
            print("Result is ", subs())
        elif(op == '*'):
            print("Result is ", multiplication())
        elif(op == '/'):
            print("Result is ", division())
        else:
            print("So long")
            break
    else:
        break
