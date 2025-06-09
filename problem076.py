# similar to DP of problem 31
#

target = 100
ways = {}
for amount in range(0, target+1):
    ways[amount] = 0

ways[0] = 1 # 1 way (empty/nothing) to make zero
#print(ways)

for digit in range(1, target+1):
    for amount in range(digit, target+1):
        ways[amount] += ways[amount - digit]

        #if amount == 200:
        #    print(ways[amount],"-->",end='')

# subtract 1 because our method included a sum using 1 digit only
print(f"Number of ways to make {target}:",ways[target]-1)

