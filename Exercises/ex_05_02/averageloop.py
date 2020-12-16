counter = 0
total = 0
print('Before', counter, total)
for num in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    total = total + num
    print(total, num)
print('After', counter, total, total/counter)
