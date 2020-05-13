def sort_012(l):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    nextId_0=0
    nextId_2=len(l)-1
    cur=0
    while(cur<=nextId_2):
        if (l[cur]==0):
            l[cur]=l[nextId_0]
            l[nextId_0]=0
            nextId_0+=1
            cur+=1
        elif (l[cur]==2):
            l[cur]=l[nextId_2]
            l[nextId_2]=2
            nextId_2-=1
        else:
            cur+=1
    return l
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

## Edge Cases:

test_function([1, 1, 1, 0])
test_function([0])
test_function([2, 2, 2])
test_function([2, 0])
test_function([0, 1, 2])





