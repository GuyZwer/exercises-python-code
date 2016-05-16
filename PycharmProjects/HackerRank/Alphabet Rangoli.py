'''
N = int(raw_input())

list_alphabet1 = 'abcdefghijklmnopqrstvuwxyz'
def add_dash(letters):
    return '-'.join(list(letters))

for num in range(N):
    print (add_dash(list_alphabet1[num:0:-1] + list_alphabet1[:num+1]).center(((N+1)*2)+((N-1)*2)-3,'-'))

for num in range(N-1):
    print (add_dash(list_alphabet1[(N-1)-(num+1):0:-1] + list_alphabet1[:(N)-(num+1)]).center(((N+1)*2)+((N-1)*2)-3,'-'))

'''

N = int(raw_input())

list_alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
def add_dash(letters):
    return '-'.join(list(letters))

for num in range(1,N+1):
    print (add_dash(list_alphabet1[N-1:N-num:-1] + list_alphabet1[N-num:N]).center(((N+1)*2)+((N-1)*2)-3,'-'))

for num in range(N-1):
    print (add_dash(list_alphabet1[N-1:num+1:-1] + list_alphabet1[num+1:N:1]).center(((N+1)*2)+((N-1)*2)-3,'-'))

