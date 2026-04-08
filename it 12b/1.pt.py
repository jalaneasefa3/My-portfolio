weight= float(input("enter weight in kg:"))
height= float(input("enter height in meter:"))
bmi=weight/(height**2)
print("BMI=",bmi)
if bmi<18.5 and bmi>0:
  print("under weight")
elif bmi<=24.9:
  print("normal weight")
elif bmi<=29.9:
  print("over weight")
else:
   print("obesity")    
  
