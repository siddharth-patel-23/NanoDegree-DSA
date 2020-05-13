def binary_search(input_list, target, left, right):
    if (left>right):
        return -1
    mid=(left+right)//2
    if (input_list[mid]==target):
        return mid
    
    if (input_list[left]<=input_list[mid]): ## If the left half is sorted, then search there first
        if (target>=input_list[left] and target<=input_list[mid]): ## If the target is in the left half, and left half is sorted
            ind=binary_search(input_list, target, left, mid)
            if (ind!=-1):
                return ind
        
        ind=binary_search(input_list, target, mid+1, right) ## If the target is in the right half, and left half is sorted
        if (ind!=-1):
            return ind
    else: ## If the right half is sorted, then search there first
        if (target>=input_list[mid] and target<=input_list[right]): ## If the target is in the right half, and right half is sorted
            ind = binary_search(input_list, target, mid, right)
            if (ind!=-1):
                return ind

        ind = binary_search(input_list, target, left, mid-1) ## If the target is in the left half, and right half is sorted
        if (ind!=-1):
            return ind
    return -1 ## If target not found, then  return -1
    

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if (len(input_list)==0):
        return -1
    return binary_search(input_list, number, 0, len(input_list)-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

## Normal Cases:
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

## Edge Cases:

test_function([[], 10])
test_function([[], None]) # As mentioned in the review, edge cases added






