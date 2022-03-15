from art import logo

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def calculator():
    print(logo)
    a = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    calculating_done = False
    while not calculating_done:
        operation = input("Pick an operation: ")
        b = float(input("What's the next number?: "))

        function = operations[operation]
        result = function(a, b)
        print(f"{a} {operation} {b} = {result}")
        keep_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if keep_calc == "n":
            # calculating_done = True
            calculator()
        elif keep_calc == 'y':
            a = result

calculator()

