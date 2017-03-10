def search(A,x):
    i = 0
    if x in A:
        while( A[i] != x):
            i = i + 1
        return(i)
    else:
        print("Enter number present on List")
        return(-1)
A = [1,2,3,6,5,4]
x = int(input("Enter the number whoes index ypu want find : "))
print(search(A,x))