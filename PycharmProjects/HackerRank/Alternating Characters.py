N = int(raw_input())
strN = ''
for loop in range(N):
    string = str(raw_input())
    listN = list(string)
    strN = ''
    count = 0
    for loop in range(len(string)):
        strN += listN[loop]
        if strN[-2:]=='AA':
            count += 1
        if strN[-2:]=='BB':
            count += 1
    print count
print "end"






