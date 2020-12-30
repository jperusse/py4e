def chop(lst):
    del lst[0]
    del lst[len(lst) - 1]
    return None

def middle(lst):
    new_list = lst[1:]
    new_list = new_list[:-1]
    return new_list

new_list = []
for next in range(5):
    new_list.append(next)
assert new_list == [0, 1, 2, 3, 4]
print('Initial Sample', new_list)

chop(new_list)
print('Sample has been chopped', new_list)
assert new_list == [1, 2, 3]

new_list = []
for next in range(5):
    new_list.append(next)

print('Initial Sample', new_list)
mid = middle(new_list)
print('Middle has been extracted', mid)
assert new_list == [0, 1, 2, 3, 4]
assert mid == [1, 2, 3]

