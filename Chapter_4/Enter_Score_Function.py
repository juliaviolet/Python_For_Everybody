score=input('Enter Score:')
try:
    score1=float(score)
    def computegrade(score1):
        if score1>1.0:
            print('Out of Range')
        if score1<0.6:
                print('F')
        if score1>=0.6:
            if score1<0.7:
                print('D')
        if score1>=0.7:
            if score1<0.8:
                print('C')
        if score1>=0.8:
            if score1<0.9:
                print('B')
        if score1>=0.9:
            if score1<=1.0:
                print('A')
    computegrade(score1)
except:
    print('Out of Range')
