Height=float(input("Enter the Height in centimeters"))
Weight=float(input("Enter the Weight in kilogram"))
Height=Height/100
BMI=Weight/(Height*Height)
print("Your BMI is :",BMI)
if(BMI>0):
    if(BMI<=16):
        print("you are severely underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are Heaalthy")
    elif(BMI<=30):
        print("you are Overweight")
    else:
        print("you are severely Overweight")
else:
    print("Enter Valid Details")