import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

N = int(input())

A = [0]*N
for i in range(N):
    A[i]=int(input())



print(lcm_list(A))