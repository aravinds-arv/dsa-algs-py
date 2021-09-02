def recinsSort(seq):

    """
    Returns a list sorted in the ascending order

        Parameters:
        ----------
            l (list/array): A list or an array

        Returns:
        -------
            l (list/array): The sorted list is returned
    """
    
    # unlike the normal version of the insertion sort where we move from a slice of length 1 and sort bigger and bigger lists,
    # here we assume that the first k-1 terms of the sequence is already sorted and try to insert the kth term into this sequence
    # hence we start with a list of length len(seq)-1 and then we move backwards to smaller and smaller lists inserting the last elements of each slice into
    # appropriate positions

    # calling an auxillary function isort
    isort(seq, len(seq))
    return seq # after all the recursions of isort() the list would've been finally sorted and this list is returned

# the isort function is much simillar to the outer for loop in the first version of insertion sort where it was used to change the position of the slice end in each iteration
# here it does the same except that here we move backwards instead of forwards
# the function recursively calls itself while updating the value of k to k-1
# if k <= 1, then k-1 = 0/-1 which means it is either the first or the last position which would have already been sorted by then
# hence they are kept as the base cases to exit recursion
def isort(seq, k):
    if k > 1:
        isort (seq, k-1)
        insert(seq, k-1)

# this fuction is exactly the same as the while loop seen in the previous version
# it compares the value at pos with the previous value and swaps them if necessary
# it repeats this until the value which was at k has reached its appropriate position or whwn it reaches the first position
def insert(seq, k):
    pos = k
    while pos > 0 and seq[pos] < seq[pos-1]:
        (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
        pos = pos - 1

print(recinsSort([97, 45, 68, 73, 32, 81, 104]))