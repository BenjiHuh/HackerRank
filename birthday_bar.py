#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    counter = 0
    if m == 1:
        if s[0] == d:
            counter += 1
    else:
        for z in range(0, len(s) - m + 1):
            sum = 0
            for i in range(z, z + m):
                # if s[i + m] - s[i] == 0:
                #     counter += 1
                sum += s[i]
            print(sum)
            if sum == d:
                counter += 1
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
