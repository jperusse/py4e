total = 0
count = 0
imax = None
imin = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue

    total = total + inum
    count = count + 1
    if imax == None or inum > imax :
        imax = inum
    if imin == None or inum < imin :
        imin = inum

if count > 0:
    print(total, count, imax, imin)
