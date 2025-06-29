DEBUG = 1

# simple matrix for testing
M1 = [  [131, 673, 234, 103,  18],
        [201,  96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524,  37, 331]
      ]
M1 = [
    [1, 100, 100, 100, 100],
    [1,   1,   1,   1,   1],
    [1, 100,   1, 100, 100],
    [1, 100,   1, 100, 100],
    [1, 100,   1,   1,   1]
]
## Problem 82 input
#with open("./data/0082_matrix.txt", "r", encoding="utf-8") as f:
#    inputText81 = [[ int(d) for d in line.split(',')] for line in f.read().strip().split('\n')]
#
##print(inputText81)
#M1 = inputText81

#for i in range(5):
#    for j in range(5):
#        print("%3d " % M1[i][j], end='')
#    print()

size = len(M1)

# method 1
print("Method 1")

# store shortest path to i,j here
# this below is a deep copy
SP = [row[:] for row in M1]

for col in range(1, size):
    for row in range(size):
        #print(f"Calculating cell ({row},{col})")

        left = 0
        above = 0
        below = 0
        
        #print("%3d " % M1[row][col], end='')

        # from left
        left = SP[row][col-1]

        # from above
        hasAbove = row > 0
        if hasAbove:
            above_addup = M1[row-1][col]
            above = above_addup + SP[row-1][col-1]
            #print("has above")

            for a in range(row-2, -1, -1):
                above_addup += M1[a][col]
                above = min(above, above_addup + SP[a][col-1])


        # from below
        hasBelow = row < (size-1)
        if hasBelow:
            below_addup = M1[row+1][col]
            below = below_addup + SP[row+1][col-1]
            #print("has below")
            for b in range(row+2, size):
                below_addup += M1[b][col]
                below = min(below, below_addup + SP[b][col-1])
       
        min_path_value = -1
        if hasAbove and hasBelow:
            min_path_value = min(left, above, below)

        elif not hasAbove:
            min_path_value = min(left, below)

        elif not hasBelow:
            min_path_value = min(left, above)

        
        SP[row][col] = min_path_value + M1[row][col]


min_path_sum = min(v[-1] for v in SP)

if DEBUG:
    for i in range(size):
        for j in range(size):
            print("%3d " % SP[i][j], end='')
            if j == size - 1:
                min_path_sum = min(min_path_sum, SP[i][j])

        print()

print(f"The minimum path sum is: {min_path_sum}")


print("Method 2")
# method 2
# store shortest path to i,j here
# this below is a deep copy
SP2 = [row[:] for row in M1]

for col in range(1, size):
    #print(f"Processing column {col}")

    # pass 1: minimum from left
    #
    #print("Pass 1: min from left")
    for row in range(size):
        SP2[row][col] = SP2[row][col-1] + M1[row][col]

    # pass 2: minimum from above (start from top and bubble downwards)
    #
    for row in range(1, size):
        min_so_far = SP2[row][col]
        if (SP2[row-1][col] + M1[row][col]) < min_so_far:
            SP2[row][col] = SP2[row-1][col] + M1[row][col]

    # pass 3: minimum from below (start from bottom and bubble upwards)
    #
    for row in range(size-2, -1, -1):
        min_so_far = SP2[row][col]
        if (SP2[row+1][col] + M1[row][col]) < min_so_far:
            SP2[row][col] = SP2[row+1][col] + M1[row][col]


if DEBUG:
    for i in range(size):
        for j in range(size):
            print("%4d " % SP2[i][j], end='')
            if j == size - 1:
                min_path_sum = min(min_path_sum, SP2[i][j])

        print()

min_path_sum2 = min(v[-1] for v in SP2)
print(f"The minimum path sum is: {min_path_sum2}")
