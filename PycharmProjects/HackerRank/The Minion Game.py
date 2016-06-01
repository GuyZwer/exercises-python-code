s = raw_input()
vowels = 'AEIOU'
kevin_scor = 0
stuart_scor = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevin_scor += (len(s)-i)
    else:
        stuart_scor += (len(s)-i)
if kevin_scor > stuart_scor:
    print "Kevin", kevin_scor
elif kevin_scor < stuart_scor:
    print "Stuart", stuart_scor
else:
    print 'Draw'
