# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
country_stamps = set([])
for loop in range(N):
    country_stamps.add(raw_input())

print len(set(country_stamps))