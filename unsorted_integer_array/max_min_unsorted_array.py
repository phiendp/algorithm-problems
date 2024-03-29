def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_number = ints[0]
    max_number = ints[0]
    for num in ints:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num

    return (min_number, max_number)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((0, 15) == get_min_max([15, 10, 6, 0, 11, 6])) else "Fail")
print("Pass" if ((6, 20) == get_min_max([10, 15, 6, 20, 11, 6])) else "Fail")
