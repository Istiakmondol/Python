
try:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    operation=int(input("Select operation 1) add 2) sub 3) mul. 4) div 5) mod\n"))
    if operation==1:
        print(f"result is: {num1+num2}")
    elif operation==2:
        print(f"result is: {num1-num2}")
    elif operation==3:
        print(f"result is: {num1*num2}")
    elif operation==4:
        print(f"result is: {num1/num2}")
    elif operation==5:
        print(f"result is {num1%num2}")
except ZeroDivisionError as zde:
    print(zde)
except NameError as ne:
    print(ne)
except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
except Exception as main:
    print(main)
    print("Exception catch from main\n")
else:
    print("Program successfully executed")
finally:
    print("Good Day")

        