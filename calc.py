num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
operation = input("enter an operation (=,-,*,/) ")
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(f"{num1/num2:.2f}")
else:
    print("invalid operation")