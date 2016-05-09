#!/bin/python

import sys


t = int(raw_input())

for a0 in range(t):
    n = int(raw_input())
    num = 0
    for a1 in list(str(n)):
        try:
            if int(n)%int(a1) == 0:
                num += 1
            else:
                continue
        except ZeroDivisionError:
            continue
    print num
