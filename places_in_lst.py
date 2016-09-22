arr = [int(i) for i in input().split()]
x = int(input())

flag = False

for i in range(len(arr)):
    if arr[i] == x:
        print(i, end = ' ')
        flag = True

if flag == False:
    print('Отсутствует')
