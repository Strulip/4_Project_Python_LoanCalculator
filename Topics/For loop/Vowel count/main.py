string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

counter = 0

for vow in vowels:
    for let in string:
        if vow == let:
            counter += 1

print(counter)