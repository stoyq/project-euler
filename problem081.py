DEBUG = 0

# simple matrix for testing
M1 = [  [131, 673, 234, 103,  18],
        [201,  96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524,  37, 331]
      ]

# Problem 81 input
with open("./data/0081_matrix.txt", "r", encoding="utf-8") as f:
    inputText81 = [[ int(d) for d in line.split(',')] for line in f.read().strip().split('\n')]

#print(inputText81)
M1 = inputText81

#for i in range(5):
#    for j in range(5):
#        print("%3d " % M1[i][j], end='')
#    print()


# solve order: diagonals
# 00
# 10 01
# 20 11 02
# 30 21 12 03
# 40 31 22 13 40
# ...
#

if DEBUG:
# first let's try to traverse the diagonals
    for i in range(1, 2*len(M1)-1): # 0, 1, 2, 3, 4
        for j in range(i+1):
            row = i-j
            col = j
            if row < len(M1) and col < len(M1):
                print(f"{row}{col} ", end='')

        print()


# store shortest path to i,j here
#SP = [ [0 for _ in range(len(M1))] for _ in range(len(M1)) ] 
SP = M1

# initialize 0,0
#SP[0][0] = M1[0][0]
#print(SP)


for i in range(1, 2*len(M1)-1): # 0, 1, 2, 3, 4
    for j in range(i+1):
        row = i-j
        col = j

        # only work on valid cell ranges
        if row >= len(M1) or col >= len(M1):
            continue

        #print(f"Now on SP[{row}][{col}]")

        # special cases: row 0 cells have no cells above
        # #              col 0 cells have no cells to the left
        if row == 0:
            SP[row][col] += SP[row][col-1]
        elif col == 0:
            SP[row][col] += SP[row-1][col]
        else:
            # normal case with cells above and to the left
            SP[row][col] += min(SP[row-1][col], SP[row][col-1])


#for i in range(len(M1)):
#    for j in range(len(M1)):
#        print("%3d " % SP[i][j], end='')
#    print()

print("Shortest path sum is", SP[-1][-1])
