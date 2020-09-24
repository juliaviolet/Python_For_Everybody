score = input("Enter Score: ")
try:
    score1=float(score)
    if score1>1.0:
        print('Out of Range')
    elif score1<0.6:
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
except:
    print('Out of Range')
