def insSort(seq):

    """
    Returns a list sorted in the ascending order

        Parameters:
        ----------
            l (list/array): A list or an array

        Returns:
        -------
            l (list/array): The sorted list is returned
    """

    # In each scan we go through slices l[0:0], l[0:1], l[0:2] and so on
    # and in each scan we either sort the slice or leave it as it is if already sorted
    for sliceEnd in range(len(seq)):
        # for each slice we check whether the element in th e slice end is smaller than the preceeding value if so they're swaped
        # the process is repeated until the element reaches either
            # a position whereit requires no more swapping or
            # the first postion seq[0]
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos - 1

    return seq

print(insSort([97, 45, 68, 73, 32, 81, 104]))