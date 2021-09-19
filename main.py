from PIL import Image

rows = int(input('enter num of rows: '))
rule = int(input('enter num of rule: '))

COLOR_BACK = (255, 255, 255)
COLOR_MAIN = (0, 0, 0)


def fractal(rows: int, rule: int):
    x = 2 * rows + 1
    y = rows

    im = Image.new(mode="RGB", size=(x, y), color=COLOR_BACK)

    canvas = [[0 for _ in range(x)] for _ in range(y)]
    canvas2 = [['  ' for _ in range(x)] for _ in range(y)]
    arr = [0] * 8

    canvas[0][(x - 1) // 2] = 1

    # canvas2[0][(x - 1) // 2] = '██'

    im.putpixel(((x - 1) // 2, 0), COLOR_MAIN)

    for i in range(7, 0, -1):
        if rule >= 2 ** i:
            rule -= 2 ** i
            arr[i] = 1
        else:
            arr[i] = 0

    arr = arr[::-1]
    current = 0
    pxn = x + 1

    while pxn < x * y:
        current += canvas[pxn // x - 1][pxn % x - 1] * 4
        current += canvas[pxn // x - 1][pxn % x] * 2
        current += canvas[pxn // x - 1][pxn % x + 1]

        canvas[pxn // x][pxn % x] = arr[current]

        if arr[current]:
            # canvas2[pxn // x][pxn % x] = '██'
            im.putpixel((pxn % x, pxn // x), COLOR_MAIN)
        else:
            canvas2[pxn // x][pxn % x] = '  '

        pxn += 1

        while pxn % x == 0 or pxn % x == x - 1:
            pxn += 1
        current = 0
    '''
    for i in canvas2:
        for j in range(1, x - 1):
            print(i[j], end="")
        print("")
    '''
    im.show()


fractal(rows, rule)
