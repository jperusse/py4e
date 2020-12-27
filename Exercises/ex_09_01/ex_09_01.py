fname = 'words.txt'
print('Processing file: ', fname)
try:
    fh = open(fname, 'r')
except:
    print('File not found:', fname)
    quit()

key_dict = dict()
for line in fh:
    # print('line:', line.rstrip())
    words = line.split()
    for word in words:
        key_dict[word] = 0

test_word = 'book'
try:
    assert test_word in key_dict
except:
    print(test_word, 'not found in the dictionary')

print('key_dict', key_dict)
