#number checker and even odd checker
x=int(input("Enter a  number: "))
if(x>0):
    print("The number is positive")
elif(x<0):
    print("The number is negitive")
else:
    print("THe number is ZERO")
choice=input("Do you want to check if the number is even or odd? (Y/N)")
if (choice=='Y' or choice=='y'):
    if(x%2==0):
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("Ok then bye")