## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word=False
        self.children={}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char]=TrieNode()
    
    def suffixes(self, suffix = ''):
        l=[]
        if (self.is_word and suffix!=''):
            l+=[suffix]
            
        if (len(self.children)==0):
            return l
        tmp=self.children
        for char in tmp:
            l+=tmp[char].suffixes(suffix+char)
        
        return l
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root=TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        tmp=self.root
        for char in word:
            tmp.insert(char)
            tmp=tmp.children[char]
        tmp.is_word=True
        
    def find(self, prefix=None):
        ## Find the Trie node that represents this prefix
        if prefix is None:
            print("Please enter a non None-Type string")
            return None
        tmp=self.root
        for char in prefix:
            if char not in tmp.children:
                print("No words with the given prefix")
                return None
            tmp=tmp.children[char]
        return tmp
            
    



# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


## Normal Cases:

prefixNode = MyTrie.find('tr')
result=prefixNode.suffixes()
print(result)
# ['ie', 'igger', 'igonometry', 'ipod']

prefixNode = MyTrie.find('f')
result=prefixNode.suffixes()
print(result)
# ['un', 'unction', 'actory']

prefixNode = MyTrie.find('an')
result=prefixNode.suffixes()
print(result)
# ['t', 'thology', 'tagonist', 'tonym']

## Edge Cases:

prefixNode = MyTrie.find('r')
# No words with the given prefix

prefixNode = MyTrie.find('')
result=prefixNode.suffixes()
print(result)
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

prefixNode = MyTrie.find()
# Please enter a non None-Type string








