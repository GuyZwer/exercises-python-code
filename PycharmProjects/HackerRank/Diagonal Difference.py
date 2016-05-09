#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
b = []
num = 0
for a1 in range(n):
    if len(b) == n:
        break
    for a2 in range(n):
        b.append(a[a2][a1+num])
        num += 1
        if len(b) == n:
            break
c = []
num = 0
for a1 in range(n):
    c.append(a[a1][int(-(a1+1))])
    num += 1
    if len(c) == n:
        break

print abs(sum(b) - sum(c))