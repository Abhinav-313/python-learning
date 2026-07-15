import math
x=int(input("Enter the radius of the circle: "))
circumference=2*math.pi*x
area=math.pi*pow(x,2)
print(f"The circumference of the circle with radius {x}cm is {round(circumference,2)}cm and the area is {round(area,2)}cm²")