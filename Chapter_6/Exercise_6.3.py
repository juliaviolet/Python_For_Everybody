word=input('Enter word:')
counter=0
def count(word):
    for letter in word:
        if letter == 'a':
            counter=counter+1
count(word)
print(count(word))
