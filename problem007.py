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
        if p > (int(n**0.5)+1):
            break

        if n % p == 0:
            return False

    primesKnown.append(n)
    return True





candidate = 3
n = 1
while n < 10001:
    if isPrimeFast(candidate):
        n = n + 1
        print(n,":",candidate)
    candidate += 2
