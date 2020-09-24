inputfile=input('Enter a file name:')
filename= open(inputfile)
count=0
counts=dict()

for line in filename:
    line=line.rstrip()
    words=line.split()
    if not line.startswith('From '): continue
    for word in words:
        counts[word]=counts.get(word,0)+1
        address = {key: counts[key] for key in counts.keys()&{'gopal.ramasammycook@gmail.com', 'louis@media.berkeley.edu',
         'cwen@iupui.edu', 'antranig@caret.cam.ac.uk', 'rjlowe@iupui.edu', 'gsilver@umich.edu', 'david.horwitz@uct.ac.za',
         'wagnermr@iupui.edu', 'zqian@umich.edu', 'stephen.marquard@uct.ac.za', 'ray@media.berkeley.edu'}}
    temp=max(address.values())
    res=[key for key in address if address[key] == temp]
print(str(res[0])+' '+str(temp))
