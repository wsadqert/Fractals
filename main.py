from random import randint
from PIL import Image
from tqdm import tqdm

rows = int(input('enter num of rows: '))
rule = int(input('enter num of rule: '))

COLOR_BACK = (255, 255, 255)
COLOR_MAIN = (0, 0, 0)


def fractal(rows: int, rule: int):
	rule_ = rule
	print('[...] loading...', end='')

	x = 2 * rows + 1
	y = rows
	im = Image.new(mode="RGB", size=(x, y), color=COLOR_BACK)
	canvas = [[0 for _ in range(x)] for _ in range(2)]
	canvas[0][(x - 1) // 2] = 1
	arr = [0] * 8
	current = 0
	im.putpixel(((x - 1) // 2, 0), COLOR_MAIN)

	for i in range(7, 0, -1):
		if rule >= 2 ** i:
			rule -= 2 ** i
			arr[i] = 1
		else:
			arr[i] = 0
	arr = arr[::-1]

	print('', end='\r')

	for u in tqdm(range(y - 1)):
		for i in range(1, x - 1):
			current += canvas[0][i - 1] * 4
			current += canvas[0][i] * 2
			current += canvas[0][i + 1]
			canvas[1][i] = arr[current]

			if arr[current]:
				im.putpixel((i, u + 1), COLOR_MAIN)
			current = 0
		canvas[0] = [j for j in canvas[1]]


	im.show()
	im.save(f'./{str(randint(1000000, 9999999))}-{rule_}.png')


fractal(rows, rule)
