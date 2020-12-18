fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print(fname.upper() + "TO YOU - You have been punk'd!")
try:
    fhand = open(fname)
except:
    print('File not found:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
