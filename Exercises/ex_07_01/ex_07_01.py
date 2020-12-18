samples = 'C:\\Users\\xtech\\Documents\\GitHub\\py4e\\code3\\'
# file = 'mbox.txt'
file = 'mbox-short.txt'

full_path = samples + file

try:
    fh = open(full_path, 'r')
except:
    print('File not found: ' + full_path)
    quit()

print('File opened', full_path)
count = 0
for line in fh :
    if line.find('@uct.ac.za') == -1 : continue
    line = line.rstrip()
    print("'" + line + "'")
