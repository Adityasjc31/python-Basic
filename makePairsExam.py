def makePairs(l1,l2):
    return list(zip(l1,l2))

def makePairs(l1,l2):
    l3 = []
    for x,val in enumerate(l1):
        tup = (val,l2[x])
        l3.append(tup)
    return l3

print(makePairs([1,3,5,7],[2,4,6,8]))
