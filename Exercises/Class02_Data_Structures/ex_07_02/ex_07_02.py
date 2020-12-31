
fname = input('Enter a file to find the average spam confidence: ')
# fname = 'mbox-short.txt'
try:
    fh = open(fname, 'r')
except:
    print('File not found:' + fname)
    quit()
count = 0
spamconf = 0.0
avg_list = []

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        cpos = line.find(':')
        snum = line[cpos + 1:].strip()
        avg_list.append(snum)
        spamconf = spamconf + float(snum)
        # break
print('Processing file: ' + fname)
print('Count: ', count, 'Spam confidence numbers: ', 'Avg', spamconf / count, 'Min', min(avg_list), 'Max', max(avg_list))
# print(avg_list)
        