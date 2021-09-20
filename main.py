from random import randint

from PIL import Image

rows = int(input('enter num of rows: '))
rule = int(input('enter num of rule: '))

COLOR_BACK = (255, 255, 255)
COLOR_MAIN = (0, 0, 0)


def fractal(rows: int, rule: int):
    x = 2 * rows + 1
    y = rows

    im = Image.new(mode="RGB", size=(x, y), color=COLOR_BACK)

    # canvas = [[0 for _ in range(x)] for _ in range(y)]
    canvas = [[0 for _ in range(x)] for _ in range(2)]
    # canvas2 = [['  ' for _ in range(x)] for _ in range(y)]
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
    u = 0

    while u < (y - 1):
        for i in range(1, x - 1):
            current += canvas[0][i - 1] * 4
            current += canvas[0][i] * 2
            current += canvas[0][i + 1]
            canvas[1][i] = arr[current]

            if arr[current]:
                # canvas2[i // x][i % x] = '██'
                im.putpixel((i, u + 1), COLOR_MAIN)
            current = 0
        canvas[0] = [j for j in canvas[1]]
        u += 1
        print(f'\r[{u + 1}/{y} ({((u + 1) / y * 100):.5f} %)', end='')
    '''
    for i in canvas2:
        for j in range(1, x - 1):
            print(i[j], end="")
        print("")
    '''
    im.show()
    im.save(f'C:/Users/matve/Desktop/fractals/{str(randint(1000000, 9999999))}.png')


fractal(rows, rule)
