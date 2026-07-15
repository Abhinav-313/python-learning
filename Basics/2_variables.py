#using variables now
name = "Abhi" 
#printing string using f-string
print(f"Hello i am {name}")
age= 21
print(f"I am {age} years old")
height= 177.7
print(f"I am {height}cm tall")
student_status=True
if(student_status==True):
    print("I am a student")
else:
    print("I am not a student")
#___________TYPECASTING____________
height_whole=int(height)
print(f"my height without decimal is {height_whole}")
age = str(age)
age+="1"
print(age)
name=bool(name)
print(name)
mt=""
mt=bool(mt) #empty string
print(mt)