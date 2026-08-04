num1 = int(input("Enter a first number : "))
print(num1)
num2 = int(input("Enter a second number : "))
print(num2)

op = input("Enter the operation you want to excute among \"+,-,*,/\" : ")

match op:
    case "+":
        print("Addition :", num1,"+", num2,"=",num1 + num2)
    case "-":
        print("Subtraction :",num1,"-", num2,"=",num1 - num2)
    case "*":
        print("Multiplication :",num1,"*", num2,"=",num1 * num2)
    case _:
        print("Division :",num1,"/", num2,"=",num1 / num2)

