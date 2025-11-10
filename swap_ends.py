def swap_ends(L, k):
    
    if k <= 0:
        return (L.copy(), 0)
    
    listlenght = len(L)
    
    if listlenght == 0 or k > listlenght / 2:
        return (L.copy(), 0)
    
    partA = L[0:k]
    
    partB = L[k:-k]
    
    partC = L[-k:]
    
    newlist = partC + partB + partA
    
    numswaps = k
    
    return (newlist, numswaps)