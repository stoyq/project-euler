# the number in question
num = 600851475143 

# store all factors
all_factors = []


# starting possible factor
factor = 2

# we don't have to check beyond sqrt(num)
while factor * factor < num:
    if num % factor == 0:
        # factor found!
        print(factor, "is a factor")
        all_factors.append(factor)
        # update num for next iteration
        num = num // factor
        print(num, "is the new num")
    else:
        # factor is not a factor
        # increment factor
        factor = factor + 1

print(num, "is the largest prime factor")
print("all factors:", all_factors)
