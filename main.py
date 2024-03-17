def calculation(x, y, operator):
    
    try:
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
        
    except ZeroDivisionError:
        print("Division by zero is invalid!!!")
    
num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))

ops = ['+', '-', 'x', '/']
while True:
    operator = input("Enter the operator you would like to use : ")

    if operator not in ops:
        print('''Your selected operator is invalid.
              Please use one of the following symbols :
                +(addition), -(subtraction), x(multiplication), /(division)''')
        continue

    else:
        print("Calculating...")
        break


calc = calculation(num1, num2, operator)
print(calc)
    