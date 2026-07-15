#BMI calculator
h=float(input("Enter you height lil bro: "))
h_u=input("Enter the unit for height: ")
w=float(input("Enter your weight lil bro: "))
w_u=input("Enter the unit for weight: ")
if (h_u=='m' and w_u=='kg'):
    bmi=round((w/(h*h)),2)
    print("THE BMI is: ",bmi)
elif (h_u=='in' and w_u=='lb'):
    bmi=round((w/(h*h))*703,2)
    print("THE BMI is: ",bmi)
else:
    print("Mismatch units.")

print("Checking for category....")
if(bmi<=18.5):
    print("You are underweight!")
elif(bmi>18.5 and bmi<=24.9):
    print("You are healthy")
elif(bmi>24.5 and bmi<=29.9):
    print("You are overweight")
elif(bmi>30):
    print("You are obese")