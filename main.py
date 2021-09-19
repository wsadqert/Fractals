a = int(input('enter a: '))
rule = int(input('enter num of rule: '))
x = 4 * a + 3
y = int((a - a % 2) * 1.5) + 1
canvas = [[0 for j in range(x)] for i in range(y)]
canvas2 = [['  ' for j in range(x)] for i in range(y)]
canvas2[0][(x-1)//2] = '██'
canvas[0][(x-1)//2] = 1

arr = [0 for i in range(8)]
for i in range(7, 0, -1):
    if rule >= 2 ** i:
        rule-=2**i
        arr[i] = 1
    else:
        arr[i] = 0
arr = arr[::-1]
print(len(arr))
print(arr)
current = 0
pxn = x + 1

while pxn < x * y:
        current += canvas[pxn // x-1][pxn % x-1] * 4
        current += canvas[pxn // x-1][pxn % x] * 2
        current += canvas[pxn // x-1][pxn % x+1]
        canvas[pxn // x][pxn % x] = arr[current]
        if arr[current]:
            canvas2[pxn // x][pxn % x] = '██'
        else:
            canvas2[pxn // x][pxn % x] = '  '
        pxn += 1
        while pxn % x == 0 or pxn % x == x - 1:
             pxn+=1
        current = 0
for i in canvas2:
    for j in range(1, x-1):
        print(i[j], end = "")
    print("")
