A = set(raw_input().split())
ans = True
for i in range(int(raw_input())):
    newSet = set(raw_input().split())
    if not A > newSet:
       ans = False
       break
print ans

