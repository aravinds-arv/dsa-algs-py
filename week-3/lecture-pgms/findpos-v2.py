def findpos(l, v):
    """
    returns the index of the first occurrence of
    v in the list
    
    If there are no ocurences of v in list, then the function
    returns -1
    """

    # used a while instead of a for as  shown in course
    # alternative to using an else block >> set pos = -1 as deafult value before the while loop

    i = 0
    while i < len(l):
        if l[i] == v:
            pos = i
            break
        i += 1
    else:
        pos = -1
    return pos

print(findpos([1,2,3,4,3], 3))
print(findpos([1,2,3,4,3], 5))