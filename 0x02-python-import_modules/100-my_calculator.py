#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import add, sub, mul, div from calculator_1
    if len(sys.argv) - 1 != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    operator = sys.argv[2]
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
