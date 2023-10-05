#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for index in range(len(sys.argv) - 1):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
