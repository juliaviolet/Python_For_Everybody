hours=input("Enter Hours:")
rate=input("Enter Rate:")
try:
    hours1=float(hours)
    rate1=float(rate)
    def computepay(hours1,rate1):
        if hours1<=40:
            computepay=hours1*rate1
            return computepay
        elif hours1>40:
            overtime=hours1-40.0
            computepay1=overtime*(rate1*1.5)+40.0*rate1
            return computepay1
    computepay(hours1,rate1)
    computeliteral=str(computepay)
    print('Pay:','$',computepay(hours1,rate1))
except: print('Error, please enter numeric input')
