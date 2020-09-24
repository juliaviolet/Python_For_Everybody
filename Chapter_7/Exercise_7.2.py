filename=input('Enter the file name:')
filehand=open(filename,'r')
count=0
total=0
average=0
for line in filehand:
    line=line.rstrip()
    if not 'X-DSPAM-Confidence'+': ' in line: continue
    pos=line.find('X-DSPAM-Confidence'+': ')
    floatextract=(float((line[pos+21:pos+26])))
    count=count+1
    total=total+floatextract
    average=total/count
print('Average spam confidence:', average)
filehand.close()
