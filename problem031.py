# target amount for problem
target = 200

ways = {}

# initiazlise ways for 1p
for amount in range(0, target+1):
    ways[amount] = 1
ways[0] = 0

#print(ways)

for coin in [2, 5, 10, 20, 50, 100, 200]:
    #print(coin)
    subtotal = {}
    for ss in range(0, target+1):
        subtotal[ss] = 0

    for amount in range(coin, target+1):

        # number of times coin can be used to make amount
        ncoins = amount // coin
        #print(f"{coin}p can be used {ncoins}x to make {amount}")
        for j in range(1, ncoins+1):
            leftover = amount - coin * j
            #print("\t\tleftover:", leftover)
            if leftover == 0:
                subtotal[amount] += 1
            else:
                subtotal[amount] += ways[leftover]

    # update ways
    for key, value in subtotal.items():
        ways[key] += value

print(f"Number of ways to make {target}p:",ways[target])
#print(ways[77])
#print(ways[137])
#print(ways[199])


print("--- Improved Method ---")

# reset
target = 200
ways = {}
for amount in range(0, target+1):
    ways[amount] = 0

#print(ways)

for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    for amount in range(coin, target+1):
        if amount == coin:
            ways[amount] += 1
        else:
            ways[amount] += ways[amount - coin]

        #if amount == 200:
        #    print(ways[amount],"-->",end='')

print(f"Number of ways to make {target}p:",ways[target])
