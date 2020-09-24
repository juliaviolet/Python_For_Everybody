lst=[]

while True:
    numbers = input('Enter a number: ')
    if numbers == 'done':
        break
    try:
        numbers = int(numbers)
    except:
        print('Invalid input')
        continue
    lst.append(numbers)

print("Maximum:", max(lst), "\nMinimum:", min(lst))
