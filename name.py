array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
new_arr = []

total = 0
for i in array:
    num = i[0]
    for n in i:
        if n <= num:
            num = n
    total += num

print(total)
