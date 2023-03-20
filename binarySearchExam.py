def BinarySearch(Arr,l,R,X):
    if(l<=R):
        mid = (l+R)/2
        if Arr[mid] == X:
            return mid
        elif Arr[mid] < X:
            return BinarySearch(Arr,l,mid-1,X)
        else:
            return BinarySearch(Arr,mid-1,R,X)
    
    return "Not Found"