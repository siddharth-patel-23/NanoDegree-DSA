Problem_3:
This problem, as stated to be solved in time complexity of O(n*log(n)), has given the clue to be tackled by 
a variation of the merge sort algorithm. Indeed, it is a merge sort algorithm, except for the particular 
treatment if gives to the comparison of results coming from the previous recursion, if we are on the first 
level of the recursion. In this case, it does the comparison, as usual, but then starts saving the results on 
alternative lists, which are then returned as the results.

The usage of this alternative list saving is due to the fact that having the list perfectly sorted, if we start 
from the index[0] and give alternatively a value to each list, occupying this value an increasing digit position, 
we always obtain a combination that satisfies the condition of having a maximum sum of two numbers and maximum a 
digit of difference between them.

Time and Space Complexity:
As the base of the algorithm is the merge sort, having a time complexity of O(n*log(n)), and there have been no 
substantial modifications to the algorithm; just the addition of O(1) operations, the time complexity remains 
equal. As for the space complexity, if we hold the assumption that python gets automatically rid of each previous 
step auxiliary created arrays, then the space complexity is of O(n) (we have always arrays that amount to the length 
of the input array).
