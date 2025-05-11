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


candidate = 2
n = 0
while n < 10001:
    if isPrime(candidate):
        n = n + 1
        print(n,":",candidate)
    candidate += 1
