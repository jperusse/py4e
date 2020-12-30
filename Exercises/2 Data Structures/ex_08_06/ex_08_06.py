
numlist = list()
while True:
    num = input("Enter a number (press Enter to use test data [6,2,9,3,5]): ")
    if num == '':
        numlist = [6.0, 2.0, 9.0, 3.0, 5.0]
        break
        

    if num == 'done':
        break

    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    
    numlist.append(fnum)

    
if len(numlist) > 0:
    print('Max:', max(numlist))
    print('Min:', min(numlist))
