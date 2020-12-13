errmsg = "Bad score"
score = input("Enter score: ")

try:
    fscore = float(score)
except:
    print(errmsg)
    quit()

if fscore >= 0.0 and fscore <= 1.0 :
    if fscore >= 0.9 :
        print('A')
    elif fscore >= 0.8 :
        print('B')
    elif fscore >= 0.7 :
        print('C')
    elif fscore >= 0.6 :
        print('D')
    else: 
        print('F')
else:
    print(errmsg)