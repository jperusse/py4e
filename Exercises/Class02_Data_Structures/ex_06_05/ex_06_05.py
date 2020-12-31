str = 'X-DSPAM-Confidence: 0.8475 '
snum = str[(str.find(':') + 1):]
print("'" + snum + "'")
fnum = float(snum)
print(type(fnum))