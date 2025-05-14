import time
from math import isqrt

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

# we start at 3. so in the loop we can skip all even numbers. half candidates
candidate = 3
N = 2000000
total = 2
primes = [2]
while candidate < N:
    if isPrimeFast(candidate):
        total = total + candidate
        #print(candidate,"is prime")
        primes.append(candidate)
    candidate += 2
print()
end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")
print(f"The sum of all primes below {N} is {total}")

print("Check:",sum(primes))
print("Last prime under",N,"is",primes[-1])
