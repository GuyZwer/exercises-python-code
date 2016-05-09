s = ''.join(raw_input().split()).lower()
alphabet = 'abcdefghijklmnopqrstvuwxyz'

if len(''.join(set(s))) == len(alphabet):
    print 'pangram'
else:
    print 'not pangram'

