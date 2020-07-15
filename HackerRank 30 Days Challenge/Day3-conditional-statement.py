#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n>0 and n<101:    
		if n%2 != 0:
			print("Weird")
		elif (n>5 and n<21):
			print("Weird")
		else:
			print("Not Weird")