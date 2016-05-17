'''
happiness = 0
integers = map(int, raw_input().split(' '))
elements = map(str, raw_input().split(' '))
numbers = []
for num in range(2):
    numbers.append(map(str, raw_input().split(' ')))

print numbers
integersA = numbers[0]
integersB = numbers[1]

for int1 in integersA:
    if int1 in elements:
        happiness+=1
for int2 in integersB:
    if int2 in elements:
        happiness-=1


print happiness
'''
n, m = raw_input().split()
arr = [int(x) for x in raw_input().split()]
A = set([int(y) for y in raw_input().split()])
B = set([int(z) for z in raw_input().split()])
count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
print(sum(count))



