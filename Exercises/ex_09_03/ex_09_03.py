file = 'mbox.txt'
# file = 'mbox-short.txt'

try:
    fh = open(file, 'r')
except:
    print('File not found: ' + file)
    quit()

print('File opened', file)

addesses = dict()
for line in fh:
    words = line.split()

    if len(words) < 2 or words[0] != 'From': continue

    addess = words[1]
    addesses[addess] = addesses.get(addess, 0) + 1

print('Count of addresses found:', len(addesses))

print(addesses)