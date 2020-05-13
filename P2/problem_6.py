def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if (len(ints)==0):
        return None
    
    min_element=ints[0]
    max_element=ints[0]
    for i in ints:
        if (i<min_element):
            min_element=i
        if (i>max_element):
            max_element=i
    return (min_element, max_element)
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(-100, 10)]  # a list containing -100 - 9
random.shuffle(l)

print ("Pass" if ((-100, 9) == get_min_max(l)) else "Fail")

## Edge Cases:

l=[-2, -2]
print ("Pass" if ((-2, -2) == get_min_max(l)) else "Fail")

l=[0]
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l=[-20, 0]
print ("Pass" if ((-20, 0) == get_min_max(l)) else "Fail")

