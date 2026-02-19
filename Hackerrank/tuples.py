n = int(input())
numbers = tuple(map(int, input().split()))[:n]
print(hash(numbers))
