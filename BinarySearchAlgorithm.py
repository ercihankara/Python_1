#import numpy as np
# {}.format('ape') puts ape to {} in the string
# // for int division
# // for float division

import re
lower = 1
upper = 101
length = 50

''' recursive btw '''
def search(arr, low, high, desired):
    if (high >= low):
        mid = (high + low)//2
        if (desired == arr[mid]):
            return mid
        elif (desired > arr[mid]):
            return search(arr, mid+1, high, desired)
        else:
            return search(arr, low, mid-1, desired)
    else:
        return -1

''' creating the list, ordered'''
arr = [lower + x*(upper-lower)/length for x in range(length)]
#print(arr)
val = int(input("Enter the value you want to search for, between 1-100: "))
indx = search(arr, 0, len(arr)-1, val)

 ''' used to find the index of a value, if there '''
if (indx != -1):
    print("Your number's index is ", indx)
else:
    print("The number is not here :(")
