def findpos(l, v):
    """
    returns the index of the first occurrence of
    v in the list
    
    If there are no ocurences of v in list, then the function
    returns -1
    """

    # a much more shortened version for the same purpose
    # using a return statement instead of a break to exit the loop and the function itself
    # no temporary variables hence more efficient in terms of memory usage to

    for i in range(len(l)):
        if l[i] == v:
            return i
    else:
        return -1

print(findpos([1,2,3,4,3], 3))
print(findpos([1,2,3,4,3], 5))