files = 'mbox.txt', 'mbox-short.txt', 'mbox-short2.txt', 'romeo.txt'
for file in files:
    try:
        fh = open(file, 'r')
    except:
        print('File not found: ' + file)
        quit()

    print('File opened', file)

    hours = dict()
    for line in fh:
        words = line.split()

        if len(words) < 6 or words[0] != 'From': continue

        time = words[5]
        assert time.find(':') == 2 # check for a time format

        hour, minute, second = (time.split(sep=':'))
        hours[hour] = hours.get(hour, 0) + 1
        
    lst = list()
    for hour, count in hours.items():
        lst.append((hour, count))

    lst.sort()
    for hour, count in lst:
        print(hour, count)
