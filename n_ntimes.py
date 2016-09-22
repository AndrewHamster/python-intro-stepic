n = int(input())
if n == 1:
    print(1, end=' ')
else:
    count = 0
    for i in range(n):
        flag = True
        for j in range(i):
            print (i, end = ' ')
            count += 1
            if count == n:
                flag = False
                break
        if not flag:
            break
