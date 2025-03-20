num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

operation=int(input("Select operation 1) add 2) sub 3) mul. 4) div"))
if operation==1:
    print("result is: ",num1+num2)
elif operation==2:
    print("result is: ",num1-num2)
elif operation==3:
    print("result is: ",num1*num2)
else:
    print("result is: ",num1/num2)