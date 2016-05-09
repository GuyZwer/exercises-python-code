'''

N1 = int(raw_input())
N2 = raw_input()
N2 = N2.split()
sum1 = 0
for loop in range(N1):
    sum1 += int(N2[loop])
print sum1
'''
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum1 = 0
for loop in range(n):
    sum1 += arr[loop]
print sum1
