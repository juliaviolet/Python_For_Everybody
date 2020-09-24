largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == "done" :
        break
    try:
        numfloat=float(num)
    except:
        print('Invalid input')
        continue
    if smallest is None or numfloat<smallest:
        smallest=numfloat
    if largest is None or numfloat>largest:
        largest=numfloat
print('Maximum is', int(largest))
print('Minimum is', int(smallest))
