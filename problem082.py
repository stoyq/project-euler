DEBUG = 1 

# simple matrix for testing
M1 = [  [131, 673, 234, 103,  18],
        [201,  96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524,  37, 331]
      ]

# Problem 82 input
with open("./data/0082_matrix.txt", "r", encoding="utf-8") as f:
    inputText81 = [[ int(d) for d in line.split(',')] for line in f.read().strip().split('\n')]

#print(inputText81)
M1 = inputText81

#for i in range(5):
#    for j in range(5):
#        print("%3d " % M1[i][j], end='')
#    print()

size = len(M1)

# store shortest path to i,j here
# this below is a deep copy
SP = [row[:] for row in M1]

for col in range(1, size):
    for row in range(size):
        #print(f"Calculating cell ({row},{col})")

        min_path_value = 0
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
        
        if hasAbove and hasBelow:
            min_path_value = min(left, above, below)

        elif not hasAbove:
            min_path_value = min(left, below)

        elif not hasBelow:
            min_path_value = min(left, above)

        
        SP[row][col] = min_path_value + M1[row][col]







min_path_sum = SP[size-1][size-1]

for i in range(size):
    for j in range(size):
        print("%3d " % SP[i][j], end='')
        if j == size - 1:
            min_path_sum = min(min_path_sum, SP[i][j])

    print()

print(f"The minimum path sum is: {min_path_sum}")
