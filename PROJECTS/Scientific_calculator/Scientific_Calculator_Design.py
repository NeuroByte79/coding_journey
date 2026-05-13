import operator
import re

# Operators
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '//': operator.floordiv,
    '%' : operator.mod,
    '**': operator.pow,
}

# Precedence
Precedence = {
    '+': 1, '-': 1,
    '*': 2, '/': 2, '//': 2, '%': 2,
    '**': 3
}

# History(last 10)
history = []

def tokenize(expr):
    return re.findall(r'\d+|\*\*|//|[+\-*/%()]', expr)

def apply_op(values, op):
    b = values.pop()
    a = values.pop()
    result = ops[op](a, b)
    values.append(result)

def evaluate(expr):
    tokens = tokenize(expr)
    values = []
    operators = []

    for token in tokens:
        if token.isdigit():
            values.append(int(token))

        elif token == '(' :
            operators.append(token)

        elif token == ')' :
            while operators and operators[-1] != '(' :
                apply_op(values, operators.pop())
            operators.pop()

        else:  # operators

            while (operators and operators[-1] != '(' and
                   Precedence[operators[-1]] >= Precedence[token]):
                apply_op(values, operators.pop())
            operators.append(token) 
    while operators:
        apply_op(values, operators.pop())


    return values[0]


def add_to_history(expr, result):
    if len(history) == 10:
        history.pop()
    history.append(f"{expr} == {result}")


def show_history():
    print("\n---Last 10 Calculation History---")
    for item in history:
        print(item)
    print("----------------------------------\n")


# Main loop
while True:
    expr = input("Enter a expression(or 'history'/'exit'): ")
    if expr.lower() == 'exit':
        break
    elif expr.lower() == 'history':
        show_history()
        continue

    try:
        result = evaluate(expr)
        print("Result:",result)
        add_to_history(expr, result)
    except Exception as e:
        print("Error:", e)






