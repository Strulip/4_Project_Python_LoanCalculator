import math

first = math.fabs(int(input()))
second = input()

def calc_log(x, y):
    if not y or int(y) <= 1:
        return math.log(x)
    else:
        return math.log(x, int(y))

print(round(calc_log(first, second), 2))