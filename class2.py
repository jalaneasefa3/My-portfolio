hours=float(input("input hours worked: "))
pay=hours*200
if pay>5000:
    tax=0.1*pay
    netpay=pay-tax
    print(netpay)
else:
    tax=0.05*pay
    netpay=pay-tax
    print(netpay)
            
