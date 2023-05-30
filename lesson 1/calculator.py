while True:
    firstNumber = float(input("Enter first number: "))

    secondNumber = float(input("Enter second number: "))

    operator = input("Enter orperator (+, -, *, /): ")

    result = 0;

    if operator == "+":
        result = firstNumber + secondNumber
    elif operator == "-":
        result = firstNumber - secondNumber
    elif operator == "*":
        result = firstNumber * secondNumber
    elif operator == "/":
        result = firstNumber / secondNumber
    else:
        print("Operator must be in (+, -, *, /)")
        operator = input("Enter orperator (+, -, *, /): ")

    print("result = " + str(result))