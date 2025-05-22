import time
from datetime import datetime

DEBUG = 0

#
# --- The text data ---
#

inputText15 = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".split('\n')

inputText4 = """
3
7 4
2 4 6
8 5 9 3
""".split('\n')

# Problem 67 input
with open("./data/0067_triangle.txt", "r", encoding="utf-8") as f:
    inputText67 = f.read().split('\n')

#
# --- The text data, processed ---
#

# store the triangle as a list of lists
tri15 = []
for row in inputText15:
    if not row == '':
        tri15.append(list(map(int,row.split())))

# store the triangle as a list of lists
tri4 = []
for row in inputText4:
    if not row == '':
        tri4.append(list(map(int,row.split())))

# store the triangle as a list of lists
tri100 = []
for row in inputText67:
    if not row == '':
        tri100.append(list(map(int,row.split())))
# trim a bit for testing
#tri100 = tri100[0:24]

# get left number
# tri is the triangle of numbers
# row starts at 0
# i starts at 0
def left(tri, row, i):
    # need to first make sure the indices are valid
    if not row < (len(tri)-1):
        return None
    if i > row:
        return None

    # otherwise we are good to go
    return tri[row+1][i]


# get right number
# tri is the triangle of numbers
# row starts at 0
# i starts at 0
def right(tri, row, i):
    # need to first make sure the indices are valid
    if not row < (len(tri)-1):
        return None
    if i > row:
        return None

    # otherwise we are good to go
    return tri[row+1][i+1]

# brute force (slow) max
# return maximum sum from root of triangle
def maxPath(tri, row, i):
    # base case: leaf node
    if left(tri, row, i) == None and right(tri, row, i) == None:
        return tri[row][i], [tri[row][i]]

    # recursive case
    left_sum, left_path = maxPath(tri, row+1, i)
    right_sum, right_path = maxPath(tri, row+1, i+1)

    if left_sum > right_sum:
        return tri[row][i] + left_sum, [tri[row][i]] + left_path
    else:
        return tri[row][i] + right_sum, [tri[row][i]] + right_path

# dynamic programming method
# start from bottom of triangle and move up
# Careful! Lists (tri) are passed by reference
def maxPathDP(tri):
    # we'll store the max sums here
    # use shallow 2D copy so we don't affect tri (passed by reference)
    max_sums = [row[:] for row in tri]

    # and store the left/right choice here
    # use shallow 2D copy so we don't affect tri (passed by reference)
    backtrack = [row[:] for row in tri]

    for i in range(len(max_sums)-2,-1,-1):
        # go through the row
        row = max_sums[i]
        for j in range(len(row)):
            left_sum = left(max_sums,i,j)
            right_sum = right(max_sums,i,j)
            max_sums[i][j] += max(left_sum, right_sum)

            if left_sum > right_sum:
                backtrack[i][j] = 'L'
            else:
                backtrack[i][j] = 'R'

        #print(max_sums[i])

    # now use the backtrack result to get the full path
    backtrack_list = [tri[0][0]]
    decision = backtrack[0][0]
    i_loc = 0
    if DEBUG:
        print(tri[0][0],end='')
        
    for i in range(1, len(tri)):
        if decision == 'R':
            i_loc += 1
        decision = backtrack[i][i_loc]
        if DEBUG:
            print(" ->",tri[i][i_loc],end='')
        backtrack_list.append(tri[i][i_loc])

    if DEBUG:
        print()

    return max_sums[0][0], backtrack_list




def main():
    print("Euler Problem 18")
    '''
    print(inputText15)
    print('\n'.join(str(x) for x in tri15))

    print(inputText4)
    print('\n'.join(str(x) for x in tri4))

    print(inputText67)
    print('\n'.join(str(x) for x in tri100))
    '''

    print("max of tri15 is:", maxPath(tri15, 0, 0))
    print("max of tri4 is:", maxPath(tri4, 0, 0))
    #print("max of tri100 is:", maxPath(tri100,0,0))


    print("max of tri100 using DP:",maxPathDP(tri100))

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    now = datetime.now()
    print()
    print("Last ran:", now.strftime("%H:%M"))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.6f} seconds")
