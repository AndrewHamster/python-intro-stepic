arr = [int(i) for i in input().split()]
b = []

for i in arr:
    if arr.count(i) > 1 and b.count(i) == 0:
        b.append(i)
for x in b:
    print(x, end = ' ')
