print("--- Method 1 ---")

n = 2**1000
s = str(n)
total = 0
for i in range(len(s)):
    total += int(s[i])

print(n)
print("total:",total)


print("--- Method 2 ---")
# now let's try it with manual arithmetics (no **) as an exercise
# 2^1000 has 302 digits, so we need a list of that size, at least
# we also need to keep track of the carry
#
# refresher:       1                   1
#                 128                2048
#            x      2            x      2
#            --------            --------
#                 256                4096
carry = 0
total = [0] * 305
total[0] = 2

#print(carry)
#print(total)

N = 1000 
# how many times to double
for _ in range(N-1):
    # go through each digit 1
    for i in range(len(total)):
        product = total[i] * 2 + carry
        carry = product // 10
        remainder = product % 10
        total[i] = remainder


totalStr = ''.join(str(_) for _ in total[::-1])
print(totalStr)
print("total:",sum(int(_) for _ in totalStr))




print("--- Method 3 ---")
# try another way: double a given list, and expand the list as the number get bigger
# for example: doubleNums([5, 5])
#              --> [0, 1, 1]
# (note: the numbers are reversed in order)
# but let's also do digit by digit, just like pencil and paper arithmetics
def doubleNums(nums):
    answer = []
    carry = 0
    # lets double by adding
    for digit in nums:
        dd = digit + digit + carry
        carry = dd // 10
        remainder = dd % 10
        answer.append(remainder)

    if carry > 0:
        answer.append(carry)

    return answer

result3 = [2]
for _ in range(N-1):
    result3 = doubleNums(result3)

result3reversed = ''.join(str(_) for _ in result3[::-1])
print(result3reversed)
print("total:",sum(int(_) for _ in result3reversed))
