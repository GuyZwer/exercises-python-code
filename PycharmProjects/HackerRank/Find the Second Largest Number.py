N = int(raw_input())
A = raw_input()
A = A.split()
x = A[0]
for a in range(N):
    for b in A:
        if int(x) <= int(b):
            x = b
while x in A: A.remove(x)
x = A[0]
if len(A) != 1:
    for a in range(N):
        for b in A:
            if int(x) <= int(b):
                x = b
    print x
else:
    print A[0]