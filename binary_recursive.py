def binary_recursive(A,lower,upper,x):
    mid = (lower+upper)/2
    #if x is out of range then return -1
    if (x < A[lower] | x > A[upper]):
        return -1
    #if upper and lower both are equal and A[mid] is not equal to x
    elif(lower == upper & A[mid] != x):
        return -1
    #then main algorithm
    else:
        if (A[mid] == x):
            ans = mid
        elif (x < A[mid]):
            ans = binary_recursive(A,lower,mid-1,x)
        else:
            ans = binary_recursive(A,mid+1,upper,x)
        return ans