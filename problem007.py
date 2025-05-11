def isPrime(n):
    if n == 1:
        return False
    if n <= 3:
        return True

    for i in range(2, n):
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
