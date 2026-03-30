# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
items={}

for _ in range(n):
    data=input().rsplit(' ',1)
    name=data[0]
    price=int(data[1])
    if name in items:
        items[name]+=price
    else:
        items[name]=price
for name,total in items.items():
    print(name,total)