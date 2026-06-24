medical_caues = input("Did you have a medical caues? (yes or no):").strip().upper()

if medical_caues == 'YES':
    print("you are allowed")
else:
    atten= int(input("enter the attendance of the student: "))

    if atten >=75:
        print("Allowed")
    else:
        print("you are not allowed")