name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = handle.read()
words=list()
counts=dict()
maximumvalue = None
maximumkey = None
for line in handle:
    if not line.startswith('From: '): continue
    line = line.split()
    words.append(line[1])
for word in words:
           counts[word] = counts.get(word, 0) + 1
for key,value in counts.items() :
    if value > maximumvalue:
      maximumvalue = value
      maximumkey=key
print (maximumkey, maximumvalue)
