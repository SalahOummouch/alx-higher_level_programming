#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number=len(sys.argv) - 1
    for index in range(number):
        print(int(sys.argv[index + 1]))
