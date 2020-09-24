wording=dict()
fname = input("Enter file name: ")
fh = open(fname)


for line in fh:
    words=line.split()
    wordsindictionary=list(dict.fromkeys(words))
    print(wordsindictionary)
    for letter in words:
        if letter in wording:
            continue
        else:
            print('string is not in dictionary')
