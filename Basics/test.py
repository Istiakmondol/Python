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