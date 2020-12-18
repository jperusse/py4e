
fh = open('mbox-short.txt')

for line in fh:
    line_stripped = line.rstrip()
    line_upper = line_stripped.upper() 
    print(line_upper)
