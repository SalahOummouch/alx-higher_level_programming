#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print("0{}, ".format(number),  end="")
    elif ((number % 10) * 10 + (number // 10)) > number:
        print("{}".format(number), end=", " if number < 89 else "\n")
