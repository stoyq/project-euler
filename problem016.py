n = 2**1000
s = str(n)
total = 0
for i in range(len(s)):
    total += int(s[i])

print(n)
print("total:",total)
