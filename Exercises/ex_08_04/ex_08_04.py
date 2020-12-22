

fname = 'romeo.txt'
sorted_wl = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

try:
    fh = open(fname, 'r')
except:
    print('File not found:', fname)
    quit()

unique_words = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

unique_words.sort()
assert unique_words == sorted_wl
print('Sorted list \n', unique_words)
            