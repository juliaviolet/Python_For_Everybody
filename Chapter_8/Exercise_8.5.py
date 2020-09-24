filename= open('mbox-short.txt')
count=0
for line in filename:
    line=line.rstrip()
    words=line.split()
    if len(words)<3 or not line.startswith('From '): continue
    count=count+1
    print(words[1])
print('There were', count, 'lines in the file with From as the first word')
