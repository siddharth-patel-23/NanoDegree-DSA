Problem_5:
This problem is focused on the development of the of a trie a data structure derived from a tree, suited for a 
good ratio between time and space complexity.

Time and Space Complexity:
For the trie, time complexity of searching and inserting from a trie depends on the length of the word a that’s 
being searched for, inserted, and the number of total words, n, making the runtime of these operations O(a*n). 
Looking into the space complexity of a trie, the worst case, would be when we have a word (or words), with no 
common characters between them, hence having, a node for each letter. Resulting in a space complexity of O(n).
