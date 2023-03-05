# Calculator


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multipy
def mult(n1, n2):
    return n1 * n2


# Devide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}
def calculator():
    while True:
        try:
            num1 = float(input("What's the first number? "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for symbol in operations:
        print(symbol)
    while True:
        operation_symbol = input("Pick an operation symbol from above: ")
        if operation_symbol in operations:
            break
        else:
            print("Invalid input. Please enter a valid operation symbol.")

    while True:
        try:
            num2 = float(input("What's the next number? "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    answer = operations[operation_symbol](num1, num2)

    while True:
        more_operations = input(f"Type 'y' to continue calculating with ({num1} {operation_symbol} {num2} = ){answer}, or type 'n' to exit / start a new calculation. ")
        if more_operations == 'n':
            calculator()
        while True:
            operation_symbol = input("Pick an operation symbol from above: ")
            if operation_symbol in operations:
                break
            else:
                print("Invalid input. Please enter a valid operation symbol.")
        next_num = None
        while True:
            try:
                next_num = float(input("What's the next number? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        answer = operations[operation_symbol](answer, next_num)

        print(f"Current result: {answer}")


calculator()

