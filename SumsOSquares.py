element = int(input())
sum = element
sumOSquares = element ** 2

while not sum == 0:
    element = int(input())
    sum += element
    sumOSquares += element ** 2

print(sumOSquares)
