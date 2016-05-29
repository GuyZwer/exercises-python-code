# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
for a in list(product(map(int, raw_input().split()), map(int, raw_input().split()))):
    print a,
