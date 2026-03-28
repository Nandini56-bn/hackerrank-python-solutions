# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()
k = int(k)
s = sorted(s)
perm = permutations(s, k)
for p in perm:
    print(''.join(p))