import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n+1):
        if i != 0:
            string = []
            for x in range(0, n - i):
                string.append(" ")
            for z in range(n - i, n):
                string.append("#")
            answer = "".join(string)
            print(answer)
if __name__ == '__main__':
    n = int(input())

    staircase(n)
