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

big_key = None

for key,value in addesses.items():
    if big_key is None or value > big_value:
        big_key = key
        big_value = value
print(big_key, big_value)
