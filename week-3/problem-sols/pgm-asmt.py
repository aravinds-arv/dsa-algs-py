def expanding(l):
    for i in range(len(l)-2):
        if abs(l[i+2]-l[i+1]) <= abs(l[i+1]-l[i]):
            return False
    return True
    
def sumsquare(l):
    oddList = []
    evenList = []
    for i in l:
        if i%2 == 0:
            evenList.append(i)
        else:
            oddList.append(i)
    return([oddSum(oddList), evenSum(evenList)])

def oddSum(l):
    if l == []:
        return 0 
    else:
        return l[0]**2 + oddSum(l[1:])
        
def evenSum(l):
    if l == []:
        return 0 
    else:
        return l[0]**2 + evenSum(l[1:])
        
def transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return(rez)
   
print(expanding([1,3,7,2,-3]))
print(sumsquare([-1,-2,3,7]))
print(transpose([[1,2,3],[4,5,6]]))