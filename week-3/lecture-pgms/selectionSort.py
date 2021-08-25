def selSort(l):

    """
    Returns a list sorted in the ascending order

        Parameters:
        ----------
            l (list/array): A list or an array

        Returns:
        -------
            l (list/array): The sorted list is returned
    """

    # for each scan we scan slices l[0:len(l)], l[1:len(l)], l[2:len(l)] and so on
    for start in range(len(l)):

        # assuming that the first entry has the minimum value
        minpos = start

        # we scan throughout the slice for any smaller value and if found is assigned as the new minimum
        # at the end of the loop we get the actual minimum value in the list
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                minpos = i

        # finally we swap the start value with the min value
        # this process is repeated for each slice until we reach a slice of length 1
        (l[minpos], l[start]) = (l[start], l[minpos])
    
    return l

print(selSort([97, 45, 68, 73, 32, 81, 104]))