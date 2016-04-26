class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def enque(self, item):
        return self.items.insert(0, item)
    
    def deque(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)