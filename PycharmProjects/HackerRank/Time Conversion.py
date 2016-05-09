#!/bin/python

import sys

def time_PM(x,y):
    if x == '1' and y == '2':
        return x + y
    else:
        return str(int(x)+1) + str(int(y)+2)

time = raw_input().strip()
if time[-2:] == 'AM' and time[:-8] == '12':
    print str('00') + time[-8:-2]
elif time[-2:] == 'AM':
    print time[:-2]
else:
    print time_PM(time[0:-9], time[1:-8]) + time[-8:-2]


