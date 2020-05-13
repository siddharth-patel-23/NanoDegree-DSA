Problem_2:
We can search an element in one pass of Binary Search. The idea is to search if key is middle point return mid, 
or if left of the mid part is sorted and key lies between list[left] and list[mid] then search in the left else recur in list[mid+1....right]
Else same applies if the right of the mid part is sorted.


Time and Space Complexity:
The time complexity being an algorithm based on binary search is O(log(n)).
As for the space complexity, it is independent of the input, requiring solely pointers to different array locations; O(1).
