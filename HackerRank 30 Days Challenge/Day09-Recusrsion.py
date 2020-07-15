#!/bin/python3

import os

# Complete the factorial function below.
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
