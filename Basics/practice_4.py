#max without using max
x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
z=int(input("Enter the number: "))
if(x!=y and y!=z and z!=x):    
    if(x>y and x>z):
        print("MAx is ",x)
    elif(y>x and y>z):
        print("MAx is ",y)
    elif(z>x and z>y):
        print("MAx is ",z)
elif(x==y and y!=z):
    if(x>z):
        print("max is :",x)
    else:
        print("max is :",z)
elif(y==z and z!=x):
    if(y>x):
        print("max is :",y)
    else:
        print("max is :",x)
elif(z==x and y!=x):
    if(x>y):
        print("max is :",x)
    else:
        print("max is :",y)
elif(x==y and y==z):
    print("max is all three: ",x)
else:
    print("Recheck the numbers")