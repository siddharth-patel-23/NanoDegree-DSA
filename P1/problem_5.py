import sys
import hashlib
import time

class Block:
    
    def __init__(self, data, previous_hash):
      self.timestamp = time.time()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):       
      sha = hashlib.sha256()
      hash_str = "We are going to encode this string of data!".encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
    
    def __repr__(self):
        return '\n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)
    
    
class BlockChain(object):
    
    def __init__(self):
        self.tail=None
    
    def append(self, data): # Though works as a prepend operation
        if (self.tail==None):
            self.tail=Block(data, None)
        else:
#            self.tail=Block(data, self.tail) # My Previous review comment: "previous_hash should contain hash of previous block,
                                              # not the block itself. Maintain a separate pointer(next or previous) to keep track
                                              # of next or previous block."
                                              # Here, I am creating a new block and passing the hash of the current tail as the previous
                                              # hash and then finaly assigning that new block to the tail. This all is happening simultaneously
                                              # and hence I did not used seperate pointer to keep track.

            prev_hash_pointer = self.tail        # Implementing as mentioned in the review.
            self.tail=Block(data, prev_hash_pointer) 
                                             
        
    def search(self, data):
        if (self.tail==None):
            return

        tmp=self.tail
        while(tmp!=None):
            if (tmp.data==data):
                return tmp
            tmp=tmp.previous_hash
        
        return None
    
    def size(self):
        if (self.tail==None):
            return 0
        tmp=self.tail
        cnt=0
        
        while(tmp!=None):
            cnt+=1
            tmp=tmp.previous_hash
        
        return cnt
    
    def to_list(self):
        l=[]
        if self.tail is None:
            return l
        
        tmp=self.tail
        while(tmp!=None):
            l.append([tmp.data, tmp.timestamp, tmp.hash])
            tmp=tmp.previous_hash
        
        return l
    
if __name__=='__main__':
    blockchain=BlockChain()
    print(blockchain.size())
    # 0
    print(blockchain.to_list())
    # []

    blockchain.append('my balance: 0 | cash flow: +10 | final balance: 10')
    print(blockchain.size())
    # 1
    print(blockchain.to_list())
    # [['my balance: 0 | cash flow: +10 | final balance: 10', 1588073106.81978, 'a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10']]

    blockchain.append('my balance: 10 | cash flow: +25 | final balance: 35')
    blockchain.append('my balance: 35 | cash flow: -15 | final balance: 20')
    blockchain.append('my balance: 20 | cash flow: +125 | final balance: 145')
    blockchain.append('my balance: 145 | cash flow: +5 | final balance: 150')
    print(blockchain.size())
    # 5
    print(blockchain.to_list())
    # [['my balance: 145 | cash flow: +5 | final balance: 150', 1588073106.8347518, 'a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10'],
    # ['my balance: 20 | cash flow: +125 | final balance: 145', 1588073106.8347518, 'a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10'],
    # ['my balance: 35 | cash flow: -15 | final balance: 20', 1588073106.8347518, 'a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10'],
    # ['my balance: 10 | cash flow: +25 | final balance: 35', 1588073106.8347518, 'a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10'],
    # ['my balance: 0 | cash flow: +10 | final balance: 10', 1588073106.81978, 'a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10']]

    # Testing the "search function"
    print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
    # Data: my balance: 20 | cash flow: +125 | final balance: 145 
    # Timestamp: 1588073106.8347518 
    # Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10

    # Edge Cases:
    print(blockchain.search('my balance: 1000 | cash flow: +100 | final balance: 1100'))
    # None

    blockchain = BlockChain()
    print(blockchain.search('my balance: 20 | cash flow: +125 | final balance: 145'))
    # None







