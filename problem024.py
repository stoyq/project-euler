import math

# Strategy:
# { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }  10! permutations
# 2 { 0, 1, 3, 4, 5, 6, 7, 8, 9 }   9! permutations
# 27 { 0, 1, 3, 4, 5, 6, 8, 9 }     8! permutations
# 278 { 0, 1, 3, 4, 5, 6, 9 }       ... and so on
# 2783 { 0, 1, 4, 5, 6, 9 }
# 27839 { 0, 1, 4, 5, 6 }
# 278391 { 0, 4, 5, 6 }
# 2783915 { 0, 4, 6 }
# 27839156 { 0, 4 }


# function to find the i-th lexicographic permutation of digits
def lex_perm(i, digits):
    #print(f"Calling lex_perm({i},{digits})")

    # we stop when there are no more digits to grab
    # let p=len(digits) be the left-post index
    # for each possible digit in position p, there are (p-1)! total permutations [mults]
    # we can find the largest multiple [M] of (p-1)! to add to total such that TOTAL doesn't equal or exceed i
    # then that multiple [M] is the array-index of the correct digit
    p = len(digits)
    #print("p:", p)
    TOTAL = 0
    PERM = []
    while digits:
        mults = math.factorial(p-1)
        # locate the digit so that i isn't exceeded
        M = 0
        for j in range(len(digits)):
            M = j
            if TOTAL + mults < i:
                TOTAL = TOTAL + mults
            else:
                break

        #print("M:", M)
        PERM.append(digits[M])
        digits.remove(digits[M])
        #print("PERM:", PERM, "DIGITS:", digits)
        p = len(digits)
        #print("TOTAL:", TOTAL)

    #print(PERM)
    return PERM



for k in range(999997,1000003):
    print(k,":",lex_perm(k,[0,1,2,3,4,5,6,7,8,9]))
