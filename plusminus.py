import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    first = 0
    second = 0
    third = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            third += 1
        elif arr[i] > 0:
            first += 1
        else:
            second += 1
    first = first / length
    second = second / length
    third = third / length
    print(first)
    print(second)
    print(third)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)