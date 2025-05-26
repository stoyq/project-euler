# there are 10! permutations of the digits 0-9
# that is 3,628,800 permutations
import math
print(math.factorial(10))

# if the digits starts with 0, then there are 9! permutations
# that is 362,800 permutations
print(math.factorial(9))


# So the trick is to find them in lexicographic order
# 0... has 362,800 permutations
# 1... has 362,800 permutations
# 2... has 362,800 permutations
#
# So the millionth lex. perm. starts with 2...

print(1000000-362800-362800, "-th permutation with 2 at the start")

# Continuing this pattern
# 20... has 8! or 40320 permutations 
print(math.factorial(8))

# Strategy... add 9!, 8!, 7!, until we reach 1,000,000, but not exceed
#
digits = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
perm = []
total = 0
N = 9
remainder = -1
while total < 1000000 and remainder != 0:
    fact = math.factorial(N)
    #print(f"{N}! = {fact}")
    quotient = (1000000 - total) // fact
    remainder = (1000000 - total) % fact

    if remainder == 0:
        print(f"quotient({quotient})*fact({fact})",quotient*fact)
        print("perm:",perm)#perm.append(digits[quotient-1])
        print("digits:",digits)#digits.remove(digits[quotient-1])
    else:
        #print(f"^--- need {quotient} of these")
        #print("get the ", quotient+1, "-ith digit")
        perm.append(digits[quotient])
        print("current perm:", perm)
        digits.remove(digits[quotient])
        #print("digits remaining:", digits)
        print(f"addin: quotient({quotient})*fact({fact})",quotient*fact)
        total = total + quotient * fact
        N = N - 1
print("remainder:", remainder)
print(total)

# { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
# 2 { 0, 1, 3, 4, 5, 6, 7, 8, 9 }
# 27 { 0, 1, 3, 4, 5, 6, 8, 9 }
# 278 { 0, 1, 3, 4, 5, 6, 9 }
# 2783 { 0, 1, 4, 5, 6, 9 }
# 27839 { 0, 1, 4, 5, 6 }
# 278391 { 0, 4, 5, 6 }
# 2783915 { 0, 4, 6 }
# 27839156 { 0, 4 }

print("The millionth perm is:", perm, "and the ", 1000000-total, "-th perm of: ", digits)
