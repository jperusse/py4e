# file = 'mbox.txt'
file = 'mbox-short.txt'

try:
    fh = open(file, 'r')
except:
    print('File not found: ' + file)
    quit()

print('File opened', file)

days = dict()
count = 0
for line in fh:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue

    day = words[2]
    days[day] = days.get(day, 0) + 1


print(days)