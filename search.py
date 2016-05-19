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
                                    
        