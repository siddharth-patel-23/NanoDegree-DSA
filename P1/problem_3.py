import sys
import heapq as hq

class HeapNode:
    def __init__(self, char, freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None

## As python 3 doesn't support __cmp__, the below individuals are used
    def __ne__(self, other):
        return (self.freq!=other.freq)

    def __lt__(self, other):
        return (self.freq<other.freq)

    def __le__(self, other):
        return (self.freq<=other.freq)

    def __gt__(self, other):
        return (self.freq>other.freq)

    def __ge__(self, other):
        return (self.freq>=other.freq)
        
class Huffman_Coding:
    def __init__(self):
        self.heap=[]
        self.codes={}
        self.rev_codes={}
        
    
    def make_freq_dict(self, data):
        freq={}
        for char in data:
            if not char in freq:
                freq[char]=0
            freq[char]+=1
        return freq
    
    
    def make_heap(self, freq):
        for key in freq:
            node=HeapNode(key, freq[key])
            hq.heappush(self.heap, node)
            
            
    def make_tree(self):
        if (len(self.heap)==1): ## Handling the Edge Case
            node=hq.heappop(self.heap)
            
            merged=HeapNode(None, node.freq)
            merged.right=None
            merged.left=node

            hq.heappush(self.heap, merged)
            
        while(len(self.heap)>1):
            node1=hq.heappop(self.heap)
            node2=hq.heappop(self.heap)
            
            merged=HeapNode(None, node1.freq+node2.freq)
            merged.left=node1
            merged.right=node2
            
            hq.heappush(self.heap, merged)
            
    
    def assign_codes(self):
        root=hq.heappop(self.heap)
        current_code=""
        self.helper_func(root, current_code)
        
    
    def helper_func(self, root, current_code):
        if (root==None):
            return 
        
        if (root.char!=None):
            self.codes[root.char]=current_code
            self.rev_codes[current_code]=root.char
            return
        
        self.helper_func(root.left, current_code+"0")
        self.helper_func(root.right, current_code+"1")
        

    def huffman_encoding(self, data):
        if (len(data)==0): # Handling the edge case
            print("The string is Null. Please enter a valid string\n")
            return
        
        freq=self.make_freq_dict(data)
        self.make_heap(freq)
        self.make_tree()
        self.assign_codes()
        
        encoded_data=""
        for char in data:
            encoded_data+=self.codes[char]
        return encoded_data
        pass

    def huffman_decoding(self, encoded_data):
        current_code=""
        decoded_data=""
        
        for bit in encoded_data:
            current_code+=bit
            if current_code in self.rev_codes:
                char=self.rev_codes[current_code]
                decoded_data+=char
                current_code=""
        
        return decoded_data
        pass

if __name__ == "__main__":
    codes = {}

## Normal Cases:

    # Test Case 1:
    print("test case 1:\n")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    hc=Huffman_Coding()
    encoded_data = hc.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = hc.huffman_decoding(encoded_data)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 2:
    print("test case 2:\n")
    
    a_great_sentence = "Coding is my Fun and Math is my Aim"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    hc=Huffman_Coding()
    encoded_data = hc.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = hc.huffman_decoding(encoded_data)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 3:
    print("test case 3:\n")

    a_great_sentence = "Have a good day."

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    hc=Huffman_Coding()
    encoded_data = hc.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = hc.huffman_decoding(encoded_data)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
  



## Edge Cases:

    # Test Case 4:
    print("test case 4:\n")
    a_great_sentence = ""
    
    hc=Huffman_Coding()
    encoded_data = hc.huffman_encoding(a_great_sentence)

    # Test Case 5:
    print("test case 5:\n")
    a_great_sentence = "sss"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    hc=Huffman_Coding()
    encoded_data = hc.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = hc.huffman_decoding(encoded_data)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    





