fhand=open('mbox-short.txt')
counts={}
for line in fhand:
    if line.startswith('From'):
        line=line.strip()
        atpos=line.find('@')
        domain = line[atpos+1:]
        counts[domain] = counts.get(domain,0)+1
        address = {key: counts[key] for key in counts.keys()&{'gmail.com', 'media.berkeley.edu',
 'iupui.edu', 'caret.cam.ac.uk', 'umich.edu', 'uct.ac.za'}}
print(str(address))
