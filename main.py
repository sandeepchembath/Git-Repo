def calculation(x, y, operator):
    if operator == '+':
        total = x + y
        return total
    elif operator == '-':
        total = x - y
        return total
    elif operator == "x":
        total = x * y
        return total
    elif operator == '/':
        total = x / y
        return total
    
num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))

operator = input("Enter the operator you would like to use : ")

calc = calculation(num1, num2, operator)
print(calc)
    