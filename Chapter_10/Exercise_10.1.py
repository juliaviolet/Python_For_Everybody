fhand = open('mbox-short.txt')
counts=dict()
maximumvalue = 0
maximumkey= 0


for line in fhand:
    if not line.startswith('From: '): continue
    line = line.split()
    for word in line:
        counts[word] = counts.get(word, 0) + 1
tup1=(sorted([(k,v) for (k,v) in counts.items()][5:6], reverse=True)[0])
print(tup1)
