print ("Hello World")


## this is the single line comment
''' 
    Welcome to this
    new course
'''


## Case sensitivity
name="Istiak"
Name="Nayem"
print(name)
print(Name)


## Indentation
age=33
if(age==32):
    print(age)
else:
    print("false")


## line continuation
total=1+2+3+4+5+6+\
5+6+7
print(total)


## Multiple statement in a single line
x=5;y=10;z=x+y
print(z)


## type inference
variable=10
print(type(variable))
variable="name"
print(type(variable))
variable='b'
print(type(variable))


## code example of indentation
if True:
    print("correct indentation")
    if False:
        print("Printing for false")
    print("inside of the parent if")
print("global print")

##Declaring and assigning Variablea
age=25
height=5.7
name="Istiak"
is_student=True
##printing the variables
print("Age: ",age)
print("Height: ",height)
print("Name: ",name)
print("Student: ",is_student)

##Type checking and Conversion
type(height)
##type conversion
age=25
print("Age is: ",age)
print("The type of age variable is: ", type(age))
age_str=str(age)
print("The type of age_str variable is: ", type(age_str), age)
##type conversion
age_new='25'
print(type(int(age_new)),age_new)

##Dynamic Typing
var=10
print(var, type(var))
var="hello"
print(var, type(var))
var=10.5
print(var, type(var))

## input
age=input("What is the age of that person:")
print("input thaken as ",type(age))
age=int(age)
print("the age is: ",age ,"it is after type conversion",type(age))