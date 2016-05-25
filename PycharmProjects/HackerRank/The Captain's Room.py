'''# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(raw_input())
rooms_numbers = map(int, raw_input().split())
rooms_list = set([x for x in rooms_numbers if rooms_numbers.count(x) > 1])
print set(rooms_numbers).difference(rooms_list).pop()
'''
from collections import Counter
K, a = input(), Counter(map(int, input().split()))
print(*[i if a[i] == 1 else '' for i in a.elements()], sep='')

