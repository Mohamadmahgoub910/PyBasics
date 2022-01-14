#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    inp = int(input().strip())
    if (inp % 2 == 1) | (6 <= inp <= 20):
        print("Weird")
    elif inp >= 2 & inp <= 5:
        print("Not Weird")
    elif inp > 20:
        print()
# problem link ==> https://www.hackerrank.com/challenges/py-if-else?isFullScreen=true
