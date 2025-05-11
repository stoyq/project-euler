N = 100

# sum of squares
#s1 = sum([i*i for i in range(N+1)])
s1 = sum(i*i for i in range(N+1))

# square of sum
#s2 = pow(sum([i for i in range(N+1)]), 2)
s2 = sum(range(N+1)) ** 2

# difference
print(s2-s1)
