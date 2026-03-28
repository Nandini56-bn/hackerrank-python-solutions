# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k = input().split()
k = int(k)
s = sorted(s)
for i in range(1, k + 1):
    comb = combinations(s, i)
    for c in comb:
        print(''.join(c))