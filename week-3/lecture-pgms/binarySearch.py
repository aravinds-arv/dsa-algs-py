def bSearch(seq, v, l, r):
    """
    Returns whether an element exists within a given range/slice of a sorted sequence

        Parameters:
        ----------
            seq (list/array): A list or an array
            v (int): An integer value to be searched for
            l (int): An integer(index) value representing the left limit of the slice
            r (int): An integer(index) value representing the right limit of the slice 

        Returns:
        -------
            (bool): A boolean value of either True or False depending on whether the search encounters the required value
    """
    
    # assuming that the seq passed is sorted in increasing or decreasing order

    # If the indices are equal it would mean that slice is of length 1 and thus the search failed
    if l-r == 0:
        return False

    # the middle value is obtained by integer division of the sum of l and r
    mid = (l+r)//2
    
    # if value at some point equals the mid value our search succeds and the function exits
    if v == seq[mid]:
        return True

    # if it is equal we compare the values of v and mid to decide which half must be search next
    if v < seq[mid]:
        return bSearch(seq, v, l, mid)
    else:
        return bSearch(seq, v, mid+1, r)

print(bSearch([0,1,2,3,3,4,5,6,7,8,9], 6, 0, 11))
print(bSearch([0,1,2,3,3,4,5,6,7,8,9], 3, 0, 11))
print(bSearch([0,1,2,3,3,4,5,6,7,8,9], 10, 0, 11))
