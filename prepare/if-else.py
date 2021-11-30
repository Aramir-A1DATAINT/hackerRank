#!/bin/python3

'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

import math
import os
import random
import re
import sys

def weird(n):
    if n % 2 != 0:
        print('Weird')
    else:
        if n > 20:
            print('Not Weird')
        elif n > 5:
            print('Weird')
        else:
            print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())
    weird(n)

