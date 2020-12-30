files = 'mbox.txt', 'mbox-short.txt', 'mbox-short2.txt'
for file in files:
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

    # print(addesses, '\n')
    lst = list()
    for key, value in addesses.items():
        lst.append((value,key))
    # print(lst)
    lst.sort(reverse=True)
    bigvalue, bigkey  = lst[0]
    # print(lst[0])
    print(bigkey, bigvalue)
