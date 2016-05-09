#!/bin/python

import sys

c = '#'
n = int(raw_input().strip())
for a in range(n):
    print (' '*((n-1)-a))+c+(c*a)