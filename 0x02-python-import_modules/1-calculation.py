#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1.py
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculator_1.py.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_1.py.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_1.py.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_1.py.div(a, b)))
