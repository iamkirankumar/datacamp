import numpy as np

def mult(a,b):
    a *= b
    return a

x = np.array([1,2])

print(mult(x,4))
print(x)