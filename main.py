import addition, division, multiplication, subtraction

print(addition.Add(10,2))
print(division.Divide(10,2))
print(multiplication.Multiple(10,2))
print(subtraction.Subtract(10,2))

try:
    selection = input("Select: (+, -, x, /)")
    if type(selection) != str:
        raise Exception("The input is not a string.")
    else:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        if(selection == "+"):
            print("RESULT = ", addition.Add(num1, num2))
        if(selection == "-"):
            print("RESULT = ", subtraction.Subtract(num1, num2))
        if(selection == "x"):
            print("RESULT = ", multiplication.Multiple(num1, num2))
        if(selection == "/"):
            print("RESULT = ", subtraction.Subtract(num1, num2))
    
except Exception:
    print("Please specify only with (+, -, *, /)")