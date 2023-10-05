#!/usr/bin/python3
if __name__ == "__main__":
    import add_0
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add_0.add(a, b)))
    print("{} - {} = {}".format(a, b, add_0.sub(a, b)))
    print("{} * {} = {}".format(a, b, add_0.mul(a, b)))
    print("{} / {} = {}".format(a, b, add_0.div(a, b)))
