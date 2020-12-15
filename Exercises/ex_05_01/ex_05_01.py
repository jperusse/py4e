total = 0
count = 0
while True :
    num = input('Enter a number: ')
    if num == 'done' :
        break

    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue

    total = total + inum
    count = count + 1

if count > 0:
    print(total, count, total/count)


