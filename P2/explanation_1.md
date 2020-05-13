Problem_1 (sqrt):
The implementation relies on dividing the search space in two parts and checking at each 
time if the mid point power of 2 is bigger or smaller than the given number. The number is 
divided every time by 2 and checked after squaring. After we get a number less, then we check 
the mid+1 and mid-1. Hence, returning the mid value. We use a binary search implementation.

Time and Space Complexity:
The time complexity of the problem is O(logn) as we divide our no. by 2 every time.
There is no extra space required for the operation rather than O(1). Resulting the space complexity
to be O(1).










