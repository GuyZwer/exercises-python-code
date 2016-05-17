happiness = 0
integers = map(int, raw_input().split())
elements = map(int, raw_input().split())
numbers = []
for num in range(integers[1]):
    numbers.append(map(int, raw_input().split()))

integersA = numbers[0]
integersB = numbers[1]

for int1 in integersA:
    if int1 in elements:
        happiness+=1
for int2 in integersB:
    if int2 in elements:
        happiness-=1


print happiness




