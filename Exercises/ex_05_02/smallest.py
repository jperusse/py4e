smallest_so_far = None
print('Before', smallest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far == None or num < smallest_so_far:
        smallest_so_far = num

    print(smallest_so_far, num)
print('After', smallest_so_far)
