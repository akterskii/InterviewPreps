class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key
        
class LRUCache:

    def __init__(self, capacity: int):
        
        self.dict_ = {}
        self.first = Node(None, None)
        self.last = Node(None, None)
        
        self.first.prev = self.last
        self.last.next = self.first
        self.capacity = capacity
        
        
    def get(self, key: int) -> int:
        if key in self.dict_:
            
            pr = self.dict_[key].prev
            nex = self.dict_[key].next
            nex.prev = pr
            pr.next = nex
            
            pr = self.first.prev
            self.dict_[key].next = self.first
            self.dict_[key].prev = pr
            pr.next = self.dict_[key]
            self.first.prev = self.dict_[key]
                        
            return self.dict_[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict_:
            self.dict_[key] = Node(key, value)
        else:
            self.dict_[key].val = value
            pr = self.dict_[key].prev
            nex = self.dict_[key].next
            
            pr.next = nex
            nex.prev = pr
        
        # move forward
        pr = self.first.prev
            
        self.dict_[key].prev = pr
        self.dict_[key].next = self.first
                
        pr.next = self.dict_[key]
        self.first.prev = self.dict_[key]
        # capacity
        if len(self.dict_) > self.capacity:
            last = self.last.next
            nex = last.next
            self.last.next = nex
            nex.prev = self.last
            
            self.dict_.pop(last.key, None)
                    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)