def define_number():
    number = float(input())
    if number < 0:
        return "negative"
    if number > 0:
        return "positive"
    if number == 0:
        return "zero"

print(define_number())