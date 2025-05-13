import time
from math import isqrt

def isPrime(n):
    if n == 1:
        return False
    if n <= 3:
        return True

    # only need to check up to sqrt(n)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


# Faster prime test
# - only test with known primes
# - stop at sqrt(n)
primesKnown = [2, 3]
def isPrimeFast(n):
    if n == 1:
        return False
    if n <= 3:
        return True

    for p in primesKnown:
        if p > (isqrt(n)+1):
            break

        if n % p == 0:
            return False

    primesKnown.append(n)
    return True




start = time.perf_counter()
candidate = 3
n = 1
N = 10001
print(f"Calculating the {N}-th prime number")
print("\n--- Running isPrime() ---")
while n < N:
    if isPrime(candidate):
        n = n + 1
        print(f"{n}-th prime is {candidate}".ljust(40),end='\r')
    candidate += 2
print()
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")


print("\n--- Running isPrimeFast() ---")
start = time.perf_counter()
candidate = 3
n = 1
while n < N:
    if isPrimeFast(candidate):
        n = n + 1
        print(f"{n}-th prime is {candidate}".ljust(40),end='\r')
    candidate += 2
print()
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")
