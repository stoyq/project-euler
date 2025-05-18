import math

# The number of ways to order 20 R's and 20 D's is
# 40! / (20! * 20!)
# 40! is the total number of permutations
# we divide out 20! twice, each for indistinguishable reorderings of R's and D's
print(math.factorial(40)/(math.factorial(20)**2))
