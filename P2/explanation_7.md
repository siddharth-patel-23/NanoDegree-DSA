Problem_7:
It is similar to problem 5, except for the edge cases, like "root handler", and 
working with a hierarchy of web pages instead of strings. This problem is focused on 
the development of the of a trie a data structure derived from a tree, suited for a 
good ratio between time and space complexity.

Time and Space Complexity:
For the trie, time complexity of searching and inserting from a trie depends on the length of the 
path n that’s being searched for, inserted, making the runtime of these operations O(n). Looking 
into the space complexity of a trie, the worst case, would be when we have a path (or paths), with 
no common folders between them, hence having, a node for each path block (path between forward slashes). 
Resulting in a space complexity of O(n).
