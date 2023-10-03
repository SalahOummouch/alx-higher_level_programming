#!/usr/bin/python3
for char_ascii in range(ord('a'), ord('z') + 1):
    if char_ascii != ord('e') and char_ascii != ord('q'):
        print("{}".format(chr(char_ascii)), end='')
