# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
N_student = map(int, raw_input().split())
B = int(raw_input())
B_student = map(int, raw_input().split())

print len(set(N_student).intersection(B_student))