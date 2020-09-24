count=0
total=0
average=0
while True:
    num=input('Enter a number:')
    if num == "done":
        break
    try:
        count=count+1
        total=total+float(num)
        average=total/count
    except:
        count=count-1
        print('Invalid input')
        continue
print('Count:', count)
print('Total:', total)
print('Average:', average)
