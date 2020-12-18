samples = 'C:\\Users\\xtech\\Documents\\GitHub\\py4e\\code3\\'
# file = 'mbox.txt'
file = 'mbox-short.txt'

full_path = samples + file

try:
    fh = open(full_path, 'r')
except:
    print('File not found: ' + full_path)
    quit()
count = 0
max_lines = 5
print('File opened', full_path)
for line in fh:
    print(line.rstrip().upper())
    count = count + 1
    if count > max_lines:
        break
print('All done')