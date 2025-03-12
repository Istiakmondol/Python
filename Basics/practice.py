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

## Arithmathic Operator
a=11
b=5
add_result=(a+b)
sub_result=(a-b)
mul_result=(a*b)
div_result=(a/b)
mod_result=(a%b)
floor_div_result=(a//b)
exponent_result=(a**b)

print("Add Result is: ",add_result)
print("Sub Result is: ",sub_result)
print("Mul Result is: ",mul_result)
print("Div Result is: ",div_result)
print("Mod Result is: ",mod_result)
print("Floor  is: ",floor_div_result)
print("Exponent Result is: ",exponent_result)

## (==) Comparison Operator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

if(a==b):
    print("both are equal")
else:
    print("The numbers are: ")
    print("a = ",a,"b =",b)

## (==)Comparison Operator
name1="Istiak"
name2="istiak"##case sensative
name1==name2

## (!=)Comparison Operator
name1="Istiak"
name2="istiak"##case sensative
name1!=name2

## (>) greater than Comparison Operator
a=25
b=23
if a>b:
    print(a,"is grater then",b)
else:
    print(b,"is grater then",a)

## (<) Less than Comparison Operator
a=21
b=23
if a<b:
    print(a,"is less then",b)
else:
    print(b,"is less then",a)


## (>=) greater than equal Comparison Operator
a=21
b=23
if a>=b:
    print(a,"is greater than or equal then",b)
else:
    print(b,"is greater than or equal then",a)

## (>=) less than equal Comparison Operator
a=21
b=23
if a<=b:
    print(a,"is less than or equal then",b)
else:
    print(b,"is less than or equal then",a)


## And operator
a=10
b=12
if(a==10 and b==12):
    print(True)
else:
    print(False)
    
## Or operator
a=10
b=12
if(a==10 or b==12):
    print(True)
else:
    print(False)

## if, elif, & else Conditional Statements
age=20
if age>=18:
    print("you are eligible for this 18+ content")
elif age<18:
    print("you are not allowed for this content")
else:
    print("Try Again...")


##Nested condition
##Leap year example
year=int(input("enter a year: "))
if year % 4 == 0:
    if (year % 100==0) and (year % 400 == 0):
        print(year,"is leap year")
    elif (year%100==0) and (year%400!=0):
        print(year,"is not leap year")
    else:
        print(year,"is leap year")
else:
    print(year,"is not leap year")
