def safe_print_list(my_list=[], x=0):
    result = 0
    multiplier = 1
    for i in range(x):
        try:
            item = int(my_list[i])
            result += item * multiplier
            multiplier *= 10
        except (ValueError, IndexError):
            return result
    return result
