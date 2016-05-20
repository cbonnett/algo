def b_search(alist, item):
    """
    Binary search to be used on sorted list
    :type alist: list
    :rtype: bool
    """
    found = False
    firstpoint = 0
    endpoint = len(alist) -1
    while (not found) and (endpoint >= firstpoint):
        midpoint = (firstpoint + endpoint)//2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] > item:
            endpoint = midpoint - 1
        else :
            firstpoint = midpoint + 1
    return found
                        
                        
def rec_b_search(alist, item):
    """"
    Recursive Binary search to be used on sorted list
    :type alist: list
    :rtype: bool
    """
    if len(alist) == 0:
        print 'false'
        return False
    else:
        begin = 0
        end = len(alist)-1
        midpoint = (begin + end)//2
        if alist[midpoint] == item:
            print 'true'
            return True
        elif alist[midpoint] > item:
            return rec_b_search(alist[:midpoint], item)
        else:
            return rec_b_search(alist[midpoint +1:], item)
            
def string_hash(astring, table_size):
    """
    Postion weighted string hash
    :type astring: str
    :type table_size: int
    :rtype int 
    """
    
    sum = 0
    for i, char in enumerate(list(astring)):
        sum = sum + i*ord(char)
    return sum % table_size
    
    
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self, key, value):
        hashvalue = self.hash_function(key, self.size)
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hasvalue] == key:
               self.data[hashvalue] = value
            else:
                new_hashvalue =  rehash_function(key + 1, self.size)
                while self.slots[new_hashvalue] !=None:
                    new_hashvalue = self.rehash_function(new_hashvalue, self.size)
                
                if self.slots[new_hashvalue] == None:
                    self.slots[new_hashvalue] = key
                    self.data[new_hashvalue] = value
                else:
                    self.data[new_hashvalue] = value

    def get(self, key):
        lookvalue = self.hash_function(key, self.size)
        
        data = None
        found = False
        stop = False
        startpos = lookvalue
        
        while (self.slots[startpos] !=None) and (not found) and (not stop):
            if self.slots[startpos] == key:
                data = self.data[startpos]
                found = True
        else:
            startpos = self.rehash_function(startpos, self.size)
            if startpos == lookvalue:
                stop = True
            
        return data
     
    def hash_function(self, key, table_size):
        return key % table_size
        
    def rehash_function(self, key, table_size):
        return (key + 1) % table_size 
    
    def __setitem__(self, key, value):
        return self.put(key, value)
        
    def __getitem__(self, key):
        return self.get(key)