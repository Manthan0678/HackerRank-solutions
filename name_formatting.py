#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    if 0<len(s)<1000:
        words = s.split(' ')
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
