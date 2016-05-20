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
        