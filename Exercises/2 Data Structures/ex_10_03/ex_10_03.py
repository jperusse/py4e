import string

files = 'filterout.txt', 'romeo.txt', 'mbox-short.txt', 'mbox-short2.txt', 'romeo-full.txt', 'mbox.txt'
for file in files:
    try:
        fh = open(file, 'r')
    except:
        print('File not found: ' + file)
        quit()

    print('File opened', file)

    letters = dict()
    for line in fh:
        # strip line of all spaces, digits and punctuation
        line = line.translate(str.maketrans('', '', string.whitespace))
        line = line.translate(str.maketrans('', '', string.digits))
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        
        # now build the dictionary of a-z frequencies
        for let in line:
            letters[let] = letters.get(let, 0) + 1

    # print(letters)
    if len(letters) == 0: continue

    tmplist = list()
    for k, v in letters.items():
        tmplist.append((v,k))

    # print(tmplist)
    tmplist.sort(reverse=True)
    for count, let in tmplist:
        print(let,count)

