fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
emails = dict()

for line in fhand:
    if line.startswith('From'):
        line=line.split()
        if len(line)>=5:
            str = line[5]
            str = str.split(':')
            hour = str[0]
            emails[hour] = emails.get(hour,0)+1
hourslist=[]
for hour, count in emails.items():
     hourslist.append((hour,count))
     hourslist.sort()
for hour, count in hourslist:
     print (hour, count)
