import math

DEBUG = 0

print("--- Using Python math library ---")
n = math.factorial(100)
s = str(n)
total = 0
for i in range(len(s)):
    total += int(s[i])

print("100! is",n,"and the sum of all the digits is",total)

# one liner practice
print("\n--- One liner practice ---")
total2 = sum(int(d) for d in str(math.factorial(100)))
print("total2:", total2)


# manual math practice with carry
print("\n--- Manual math practice ---")

# given 2 string digits, perform pen-and-paper math
#
#               321
#            x  867
#          --------
#              2247
#             1926
#            2568
#          --------
#            278307
#

# example: multiply_one_digit('1234', '2') -> '2468'
def multiply_one_digit(L, D):
    carry = 0
    result = []
    for i in range(len(L)-1, -1, -1):
        #if DEBUG:
        #    print(int(D) * int(L[i]))
        total = int(D) * int(L[i]) + carry
        quotient = total // 10
        remainder = total % 10
        carry = quotient
        result = [ remainder ] + result
        '''
        prod = int(D) * int(L[i])
        quotient = prod // 10
        remainder = prod % 10
        result = [remainder + carry] + result
        carry = quotient
        '''
    if carry:
        result = [carry] + result
    return ''.join(str(c) for c in result)

# example: add_two_numbers('111', '222') -> '333'
def add_two_nums(A, B):
    i, j = len(A)-1, len(B)-1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        d1 = int(A[i]) if i >= 0 else 0
        d2 = int(B[j]) if j >= 0 else 0

        D = d1 + d2 + carry
        quotient = D // 10
        remainder = D % 10
        
        result = [ remainder ] + result
        i = i-1
        j = j-1
        carry = quotient

    return ''.join(str(d) for d in result)


# example: add_many_digits(['111', '222', '333']) -> '666'
def add_many_digits(D):
    result = '0'
    for d in D:
        result = add_two_nums(result, d)
    return result

# example: multiply_many_digits('7', '5123') -> '35861'
def multiply_many_digits(L, M):
    to_add = []
    zeros = 0
    for m in range(len(M)-1, -1, -1):
        if DEBUG:
            print(multiply_one_digit(L,M[m])+'0'*zeros)
        to_add.append(multiply_one_digit(L,M[m])+'0'*zeros)
        zeros += 1
    
    return add_many_digits(to_add)
    '''
    result = '0'
    for _ in range(int(L)):
        result = add_two_nums(result, M)
    return result
    '''
print(multiply_one_digit('5123', '7'))
print(multiply_one_digit('19','9'))
print(multiply_many_digits('401','100'))
#print(multiply_many_digits('5123', '432'))
print(add_two_nums('12345','9876'))
print(add_two_nums('0','1000'))

# now let's try to compute the factorial
F = 100 
result = '1'
for d in range(1, F+1):
    result = multiply_many_digits(str(d), result)
print(f"{F}! is {result}")
print("sum of all digits is", sum(int(d) for d in result))

print("check:",math.factorial(F))
