#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number=len(sys.argv) - 1
    sum = 0
    for index in range(number):
        sum += int(sys.argv[index + 1])
    print(sum)
