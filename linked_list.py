class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next= None
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
       
    def set_data(self, newdata):
        self.data = newdata
        
    def set_next(self, newnext):
        self.next= newnext
        
class Unordered_list:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
         
    def lenght(self):
        count = 0
        temp = self.head
        while temp != None:
             count = count + 1
             temp = temp.get_next()
        return count
    
    def search(self, item):
        found = False
        temp = self.head
        while temp !=None and not found:
            if temp.get_data() == item:
                found = True
            else:
                temp = temp.get_next()
        return found 
        
    def delete(self, item):
        found = False
        next = self.head
        prev = None
        while next != None and not found:
            if next.get_data() == item:
                found = True
                if next.get_next() !=None:
                    prev.set_next(next.get_next())
                else:
                    prev.set_next(None) 
            else:
                prev = next
                next = next.get_next()
                   
    
    
    