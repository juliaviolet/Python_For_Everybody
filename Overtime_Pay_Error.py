hours=input("Enter Hours:")
rate=input("Enter Rate:")
try:
    hours1=float(hours)
    rate1=float(rate)
    if hours1<=40:
        pay=hours1*rate1
        pay1=str(pay)
        print('Pay:'+'$'+pay1)
    elif hours1>40:
        overtime=hours1-40.0
        pay2=overtime*(rate1*1.5)+40.0*rate1
        pay3=str(pay2)
        print('Pay:'+'$'+pay3)
except:
    print('Error, please enter numeric input')
