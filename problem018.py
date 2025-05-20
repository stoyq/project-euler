import time
from datetime import datetime

''' This code doesn't work (yet) and then I realize I don't need a tree. Commenting out
# create a class to define a node with left and right children
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # add a new node using level-order insertion
    # return True if successful, otherwise return False
    def add(self, value):
        # check if left is empty. if so, add it here
        if self.left is None:
            self.left = Node(value)
            return True
        
        # now check if right is empty. if so, add it here
        elif self.right is None:
            self.right = Node(value)
            return True

        # else, we have to recursively find a spot in the children
        else:
            if self.left.add(value):
                return True
            elif self.right.add(value):
                return True
            else:
                # I don't think we'll ever reach this case
                return False

    # for debugging purpose, used by print()
    def __str__(self):
        #return f"Node(value={self.value}, left={self.left}, right={self.right})"
        return f"({self.value}, ({self.left}, {self.right}))"

'''

inputText = """
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
""".replace('\n',' ').split()


def main():
    print("Euler Problem 18")
    print(inputText)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    now = datetime.now()
    print()
    print("Last ran:", now.strftime("%H:%M"))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.6f} seconds")
