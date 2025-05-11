import math
from collections import Counter


def primeFactors(n):
    # store all factors here
    f = []
    
    # starting possible factor
    factor = 2

    # we don't have to check beyond sqrt(n)
    while factor * factor <= n:
        if n % factor == 0:
            # factor found!
            #print(factor, "is a factor")
            f.append(factor)
            # update n for next iteration
            n = n // factor
            #print(n, "is the new n")
        else:
            # factor is not a factor
            # increment factor
            factor = factor + 1
    f.append(n) 
    return f

def test(n):
    factors = primeFactors(n)
    print(n,":",factors, "check:", math.prod(factors))

def debugCounter(c):
    output = ' * '.join(f'{base}^{exp}' for base, exp in c.items())
    print(output)

multisetUnion = Counter([])
for i in range(1,21):
    #test(i)
    print(i,":",end=' ')
    debugCounter(Counter(primeFactors(i)))
    multisetUnion = multisetUnion | Counter(primeFactors(i))

smallestMultiple = 1
for number, count in multisetUnion.items():
    smallestMultiple = smallestMultiple * number ** count
print("smallest multiple:", smallestMultiple)
debugCounter(multisetUnion)
