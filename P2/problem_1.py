def sqrt(number=None):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        print("The Number entered is invalid. Please enter a valid number with non None value")
        return ""

    
    if (number<0):
        print("The number entered is negative. Please enter a non-negative number.")
        return ""
    
    
    upper_bound=number
    lower_bound=0
    while(lower_bound<=upper_bound):
        mid=(lower_bound+upper_bound)//2
        if (mid*mid==number):
            return mid
        if ((mid+1)*(mid+1)>number and (mid-1)*(mid-1)<number and mid*mid<number):
            return mid
        if (mid*mid>number):
            upper_bound=mid-1
        elif (mid*mid<number):
            lower_bound=mid+1
    
    return number
    
print ("\nPass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

## Edge Cases

print(sqrt(-500))
print(sqrt())
print(sqrt(None))





