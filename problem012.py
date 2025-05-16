import time
from datetime import datetime


# triangle number is just arithmetic series, which has a closed form solution
# e.g. 4th triangle number is 1 + 2 + 3 + 4 = 10
#     or, (4 + 5) / 2 = 10
def triangleNum(n):
    return int(n * (n + 1) / 2)

# list factors of n (not prime factors)
# e.g. factors of 28 are 1, 2, 4, 7, 14, 28
def factors(n):
    f = []
    for i in range(1,n+1):
        if n % i == 0:
            f.append(i)
    return f

# might need to use prime factors
# grab solution from Euler problem #5
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

# given a list of (sorted) prime factors
# e.g. [2, 2, 2, 3, 3, 5]
# return a list of (prime, count) pair, and the product of the (count + 1)'s
# ---> [(2,3), (3, 2), (5, 1)], 12 
def factors_count(ls):
    if not ls:
        return []

    # store results here
    exponents = []
    product = 1

    # begin counting
    count = 0
    curr = ls[0]

    for num in ls:
        if num == curr:
            count = count + 1
        else:
            # we encounter a new number
            exponents.append((curr, count))
            product = product * (count + 1)

            # reset counter and update to new number
            count = 1 
            curr = num
    exponents.append((curr, count))
    product = product * (count + 1)
    return exponents, product



def main():
    print("List triangle numbers")

    # largest so far
    nDivisors = 1
    
    # triangle number i
    ti = 1
    while nDivisors < 500:
        # calculate the i-th triangle number, and then find its prime factors
        tn = triangleNum(ti)
        #fs = factors(tn)
        pfs = primeFactors(tn) # prime factors
        fc = factors_count(pfs)

        # print only if we find a bigger one than the last
        if fc[1] > nDivisors:
            nDivisors = fc[1]
            print(f"The {ti}-th triangle number ({tn}) has {fc[1]} factors:")
            print("Exponent count list:",fc)

            # display the full list of factors (expensive)
            if not True:
                fL = factors(tn)
                print(fL)
                print("Length of full factors list:", len(fL))


        else:
            print(f"The {ti}-th triangle number ({tn}) has {fc[1]} factors",end='\r')
        
        # increment to next triangle number for testing
        ti = ti + 1



if __name__ == "__main__":
    start = time.perf_counter()
    main()
    now = datetime.now()
    print()
    print("Last ran:", now.strftime("%H:%M"))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.6f} seconds")
