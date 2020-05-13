def merge(list1, list2):
    l1=len(list1)
    l2=len(list2)
    if (l1==0):
        return list2
    if (l2==0):
        return list1
    i=0
    j=0
    l=[]
    while(i<l1 and j<l2):
        if (list1[i]<list2[j]):
            l.append(list1[i])
            i+=1
        else:
            l.append(list2[j])
            j+=1

    while(i<l1):
        l.append(list1[i])
        i+=1
    
    while(j<l2):
        l.append(list2[j])
        j+=1
    
    return l
        

def merge_sort(input_list):
    if (len(input_list)<=1):
        return input_list
    
    mid=(len(input_list))//2
    left=merge_sort(input_list[:mid])
    right=merge_sort(input_list[mid:])
    
    merged=merge(left, right)
    
    return merged

def rearrange_digits(input_list=None):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        print("Please enter a list type argument")
        return
    if (len(input_list)<2):
        print("The input_list should have atleast 2 elements")
        return
    
    input_list=merge_sort(input_list)
    num1=''
    num2=''
    l=len(input_list)            
    for i in range(l-1, -1, -2):
        num1+=str(input_list[i])
    for i in range(l-2, -1, -2):
        num2+=str(input_list[i])
    
    return [int(num1), int(num2)]
    
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 2, 1], [20, 1]])

## Edge Cases:

test_function([[0, 0], [0, 0]])
test_function([[1, 0, 0, 0, 0], [100, 0]]) ## The numbers are actually [100, 00], resulting in the difference of only one digit as mentioned in the problem statement.

rearrange_digits([])
# The input_list should have atleast 2 elements

rearrange_digits()
# Please enter a list type argument




