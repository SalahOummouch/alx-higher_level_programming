#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import add, sub, mul, div from calculator_1
    if len(sys.argv) - 1 != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[2]
    b = sys.argv[4]
    operator = sys.argv[2]
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    if operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
