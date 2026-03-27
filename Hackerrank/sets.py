n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "pop":
        s.remove(min(s))
    elif cmd[0] == "remove":
        val = int(cmd[1])
        if val in s:
            s.remove(val)
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))

print(sum(s))