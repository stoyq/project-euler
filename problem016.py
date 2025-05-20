n = 2**1000
s = str(n)
total = 0
for i in range(len(s)):
    total += int(s[i])

print(n)
print("total:",total)


# now let's try it with manual arithmetics (no **) as an exercise
# 2^1000 has 302 digits, so we need to a list of that size, at least
# we also need a list for carries (just like pencil and paper math)
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

