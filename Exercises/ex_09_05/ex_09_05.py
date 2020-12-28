files = 'mbox.txt', 'mbox-short.txt', 'mbox-short2.txt'
for file in files:
    try:
        fh = open(file, 'r')
    except:
        print('File not found: ' + file)
        quit()

    print('File opened', file)

    domains = dict()
    for line in fh:
        words = line.split()

        if len(words) < 2 or words[0] != 'From' or words[1].find('@') == -1: continue

        addess = words[1]
        uname, domain = addess.split(sep='@')
        # print("'" + uname + "'", "'" + domain + "'")
        if domain == '': continue

        domains[domain] = domains.get(domain, 0) + 1

    print(domains, '\n')

