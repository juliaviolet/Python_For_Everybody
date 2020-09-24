filename=input('Enter the file name:')
filehand=open(filename,'r')
for line in filehand:
    line=line.rstrip()
    fileupper=str.upper(filehand.read())
    print(fileupper)
filehand.close()
