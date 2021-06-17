"""
CodeWars - Product of consecutive Fib numbers
Author: Dante Valentine
Date: 16 June, 2021
"""

def productFib(prod):
    fib_start = 0
    fib_end = 1    

    while fib_start * fib_end <= prod:
        if fib_start * fib_end == prod:
            return(fib_start, fib_end, True)
        fib_hold = fib_start
        fib_start = fib_end
        fib_end += fib_hold
    if fib_start * fib_end > prod:
        return(fib_start, fib_end, False)

print(productFib(4895))
print(productFib(5895))


"""
#  Top Solution from codewars:
def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
"""