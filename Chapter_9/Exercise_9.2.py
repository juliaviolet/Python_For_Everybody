filename= open('mbox-short.txt')
count=0
counts=dict()
for line in filename:
    line=line.rstrip()
    words=line.split()
    if len(words)<3 or not line.startswith('From '): continue
    for word in words:
        counts[word]=counts.get(word,0)+1
        days = {key: counts[key] for key in counts.keys()&{'Thu', 'Fri', 'Sat'}}
print(str(days))
