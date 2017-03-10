def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact=fact*i
    return(fact)
x = int(input("Enter the integer the factorial you wnat : "))
print(factorial(x))