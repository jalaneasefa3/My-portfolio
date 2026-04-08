a=float(input("enter a first number"))
b=float(input("enter b second number"))
c=float(input("enter c third number"))
if a>b and b>c or b<c:
    print ("Largest number is", a,)
elif b>a and a>c or a<c:
    print("Largest number is ",b,)
else :
    print("Largest number is ",c,)
