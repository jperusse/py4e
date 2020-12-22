
# fname = input('Enter a file to find the From count: ')
fname = 'mbox-short.txt'
print('Processing file: ', fname)
try:
    fh = open(fname, 'r')
except:
    print('File not found:', fname)
    quit()

count = 0

for line in fh:
    tokens = line.split()
    if len(tokens) < 2 or tokens[0] != 'From': continue

    count = count + 1
    print(tokens[1])

if count > 0 :
    print('There were ' + str(count) + ' lines in the file with From as the first word')
    assert count == 27
else:
    print('No lines found starting with From')
        