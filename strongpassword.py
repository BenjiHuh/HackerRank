
import math
import os
import random
import re
import sys
# Complete the minimumNumber function below.
def minimumNumber(n, password):
    total = 0
    listed = list(password)
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    islower = False
    isupper = False
    hasnum = False
    hasspecial = False
    for i in range(len(listed)):
        temp = '{}'.format(listed[i])
        if temp in numbers:
            hasnum = True
            print('1')
        if temp in lower_case:
            islower = True
            print('2')
        if temp in upper_case:
            isupper = True
            print('3')
        if temp in special_characters:
            hasspecial = True
            print('4')
    if islower == False:
        total += 1
    if isupper == False:
        total += 1
    if hasnum == False:
        total += 1
    if hasspecial == False:
        total += 1   
    if total + n < 6:
        total += 6 - (n + total)
    return total

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
