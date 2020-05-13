Project Explanation
Explanation of the different project submodules

Project 1 (LRU Cache):
To maintain the order of the use of recent elements, I used list as a queue.
For storing the cache and its corresponding value, I used a dictionary. Also 
for storing the count for cache elements and maintaining the key, value pairs, 
another dictionary named 'count' is used.

Time and Space complexity:
As mentioned in the problem statement, the time complexity for get and set 
methods is O(1). I used dictionary to search for the key and its count in the 
queue, hence O(1). Also the 'del' operation in dictionary takes O(1) time.
The append and pop(0) operations used takes O(1) time, hence resulting the overall 
time complexity to be O(1).
The space complexity of the solution is O(n) where n is the capacity of the 
cache, as there is are 2 dictionaries and one queue, all resulting in the space 
complexity of O(n)


Project 2 (File Recursion):
I am not familiar with the methods given (in the precode) to find the file, so, I used regular method of my own 
to check if the file ends with the given suffix or not and also listing all the folders 
in the given directory.

Time and Space complexity
The time complexity is dependant on the number of iterations that are launched. 
Being in this case dependent on depth and width of folders, resulting in a O(d*w). 
As for the space complexity, in this case, it is directly dependent 
on the number of returns the function does, hence, the number of found files f, O(f).


Project 3 (Huffman Coding)
This compression algorithm has shown the reduction of the size by 50% and my code is divided 
in different functions handling a particular steps of the algorithm. I used the heap (by default min heap) 
data structure to retrieve the 1st two minimum elements and then used a tree data Structure to encode the 
given data.

Time and Space complexity
The space complexity is directly related to the size of the employed alphabet, in this case k, resulting in O(k).
Here the time complexity depends on the lenght of the given string and then the no. of unique characters 
in the string as to heapify the characters with the frequencies O(n*logn) time is required.
Also retrieving and pushing each elements from the heap takes O(logn) time.
So, the resulting complexity would be O(L*log(L)) (L is the length of the given string)


Project 4 (Active Directory)
The requirement to create an efficient algorithm that searches into this encapsulated structure, 
has been satisfied by a recursive algorithm.

Time and Space complexity
The time complexity of this algorithm is dependant on the number of iterations that are launched. 
Being in this case dependent on encapsulation of groups and number of users of folders, resulting in a O(g*u). 
As for the space complexity, it is directly dependent on the number of returns the function does. We use two 
arrays to store our users and groups, so our Big O grows as simple multiples of these for space.


Project 5 (BlockChain)
This project is based on the creation of a linked list. Here rather than using append, we use prepend operation 
as the link of the previous node is used in the present node and hence the list is traversed backwards.

Time and Space complexity
The time complexity for different sets of operations are as follows:
-> append (/prepend): O(1)
-> search: O(n)
-> size: O(n)
-> to_list: O(n)
Space Complexity: Depends on the no. of nodes. Hence O(n)


Project 6 (Union and Intersection)
To find efficiently the union and intersection of the linked lists, I have 
used sets.

Time and Space complexity
The time compl. of sets to check if the elements are present or not is O(1).
Hence for the following operations the time comp. is as follows:
-> Union: O(n+m) (n and m are lengths of both the lists)
-> Intersection: O(n+m) 
As mentioned sets take O(1) time to find and '.intersection' takes O(min(n, m)) time
Space Complexity does depend on the no. of node of both the elements. Hence, O(n+m)