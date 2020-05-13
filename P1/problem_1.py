# Your work here
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.dic={} # for storing the key, value pairs as cache, content
        self.count={} # for maintaining the count of the each cache elements
        self.capacity=capacity
        self.q=[] # for storing the chache elements, works as a queue
        self.size=0
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dic:
            self.count[key]+=1
            if (self.size==self.capacity):
                if (self.count[self.q[0]]>1): # if the chache element is present in the queue more than once
                    self.count[self.q[0]]-=1  # then delete it from the queue but not from the dictionary
                    self.q.pop(0)
                else:                           # if the chache element is not occuring in the queue more than once
                    del self.count[self.q[0]]   # then delete it from the dictionary for decreasing space redundancy
                    del self.dic[self.q.pop(0)]
                self.size-=1
            self.q.append(key)
            self.size+=1
            return self.dic[key]
        return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if (self.capacity==0):
            print("The capacity of cache is set to be zero. Cannot add cache elements")
            return
        if (self.size==self.capacity): # Same goes for set
            if (self.count[self.q[0]]>1):
                self.count[self.q[0]]-=1
                self.q.pop(0)
            else:
                del self.count[self.q[0]]
                del self.dic[self.q.pop(0)]
            self.size-=1
        if key not in self.dic:
            self.count[key]=1
        else:
            self.count[key]+=1
        self.dic[key]=value
        self.q.append(key)
        self.size+=1            
        pass
    
# for getting the size of the cache, uncomment to see the steps

#     def get_size(self):
#         return self.size
    
# for printing the cache at the required steps to see if the LRU_Cache is working properly, uncomment to see the steps

##    def print_cache(self):
##        return self.q

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
##print(our_cache.print_cache())

our_cache.set(2, 2);
##print(our_cache.print_cache())

our_cache.set(3, 3);
##print(our_cache.print_cache())

our_cache.set(4, 4);
##print(our_cache.print_cache())


print(our_cache.get(1))       # returns 1
##print(our_cache.print_cache())

print(our_cache.get(2))       # returns 2
##print(our_cache.print_cache())

print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
##print(our_cache.print_cache())

our_cache.set(5, 5) 
##print(our_cache.print_cache())

our_cache.set(6, 6)
##print(our_cache.print_cache())

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
##print(our_cache.print_cache())

print("New Cases added and are giving correct output as mentioned in the first review")

our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
print(our_cache.get(4))   # Expected Value = 4
print(our_cache.get(1))   # Expected Value = -1
our_cache.set(2,4)
print(our_cache.get(2))   # Expected Value = 4
our_cache.set(5,5)
print(our_cache.get(3))   # Expected Value = -1
print(our_cache.get(5))   # Expected Value = 5
our_cache.set(2,6)
print(our_cache.get(2))   # Expected Value = 6 Your Output = 4

## Edge Cases: (Added edge cases as mentioned in the first review)

our_cache=LRU_Cache(4)
print(our_cache.get(6)) # Returns -1 as the cache is empty

our_cache=LRU_Cache(0)
our_cache.set(1, 1)
print(our_cache.get(1)) # Returns -1 as the cache is empty




