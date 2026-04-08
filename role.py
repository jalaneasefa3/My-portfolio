role = input("Enter your role (Teacher or Grade number 7-12): ")

if role == "Teacher" or role == "12":
    print("Access Granted.")

elif role == "7" or role == "8" or role == "9" or role == "10" or role == "11":
    status = input("Is it class time? (yes/no): ")
    
    if status == "yes":
        print("Access Granted.")
    else:
        print("Access Denied. Not class time.")

else:
    print("Access Denied. Invalid role.")
