import math

num = int(input())

area_oct = 2 *  math.sqrt(3) * math.pow(num, 2)

volume = 1/3 * math.sqrt(2) * math.pow(num, 3)

print(f'{area_oct:.2f} {volume:.2f}')
