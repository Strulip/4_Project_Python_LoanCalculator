# put your python code here
a = int(input())
b = int(input())

counter = 0
sum_range = 0

for i in range(a, b+1):
    if i % 3 == 0:
        counter +=1
        sum_range += i
    else:
        continue

print(sum_range/counter)