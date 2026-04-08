mass=float(input("Enter your mass"))
height=float(input("Enter your height"))
BMI=mass/(height**2)
if BMI<18.5 and BMI>0:
    print("Underweight")
elif 18.5<=BMI<24.9 :
    print("Normal weight")
elif 25<=BMI<29.9:
    print("Overweight")
else:
    print("Obesity")
    
         
