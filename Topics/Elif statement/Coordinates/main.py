def find_quadrant():
    x = float(input())
    y = float(input())
    if x>0 and y>0:
        return "I"
    elif x<0<y:
        return "II"
    elif x<0 and y<0:
        return "III"
    elif x>0>y:
        return "IV"
    elif x == 0 and y == 0:
        return "It's the origin!"
    elif x == 0 or y == 0:
        return "One of the coordinates is equal to zero!"

print(find_quadrant())