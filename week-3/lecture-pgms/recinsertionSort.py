def recinsSort(seq):
    isort(seq, len(seq))
    return seq

def isort(seq, k):
    if k > 1:
        isort (seq, k-1)
        insert(seq, k-1)

def insert(seq, k):
    pos = k
    while pos > 0 and seq[pos] < seq[pos-1]:
        (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
        pos = pos - 1

print(recinsSort([97, 45, 68, 73, 32, 81, 104]))