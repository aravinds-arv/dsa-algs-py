def findpos(l, v):
    """
    returns the index of the first occurrence of
    v in the list
    
    If there are no ocurences of v in list, then the function
    returns -1
    """
    (found, i) = (False, 0)

    while i < len(l):
        if not found and l[i] == v:
            (found, pos) = (True, i)
        i += 1
    
    if not found:
        pos = -1
    
    return(pos)

print(findpos([1,2,3,4,3], 3))
print(findpos([1,2,3,4,3], 5))