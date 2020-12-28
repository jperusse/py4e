file = 'mbox.txt'
# file = 'mbox-short.txt'

try:
    fh = open(file, 'r')
except:
    print('File not found: ' + file)
    quit()

print('File opened', file)

domains = dict()
for line in fh:
    words = line.split()

    if len(words) < 2 or words[0] != 'From': continue

    # print(words)

    addess = words[1]
    split_address = addess.split(sep='@')
    if len(split_address) < 2: continue

    # print(split_address)
    domain = split_address[1]

    domains[domain] = domains.get(domain, 0) + 1

print(domains)
