
def computegrade(score):
    if score >= 0.9:
        return('A')
    elif score >= 0.8:
        return('B')
    elif score >= 0.7:
        return('C')
    elif score >= 0.6:
        return('D')
    else:
        return('F')


errmsg = "Bad score"
score = input("Enter score: ")

try:
    fscore = float(score)
except:
    print(errmsg)
    quit()

if fscore >= 0.0 and fscore <= 1.0:
    print(computegrade(fscore))
else:
    print(errmsg)
