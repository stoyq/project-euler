import time
from datetime import datetime

# generate the next number
# even: n -> n/2
# odd:  n -> 3n + 1
def next_num(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

# length of collatz sequence starting at n
# example: for n = 13, the chain length is 10
#
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# base case when n = 1, the length is 0, as there is no "length"
# 
# also, store all the pre-calculated values here so they can be re-used
collatz = { 1: 1 } # hash map to store n and length; base case 1,1
def chain_length(n):
    #print("debug n=",n,"collatz size=",len(collatz))
    # check if it exists, if not, we will calculate it
    try:
        return collatz[n]
    except KeyError:
        collatz[n] = 1 + chain_length(next_num(n))
        return collatz[n]

def generate_chain(n):
    nums = []
    while n > 1:
        nums.append(n)
        n = next_num(n)
    nums.append(n)
    return nums

def main():
    print("Project Euler #14")

    longest = 0
    longest_i = 1
    for i in range(1, 1000000):
        #print("debug i=",i)

        # Slower approach
        #chain_len = len(generate_chain(i))

        # Faster (using hash map)
        chain_len = chain_length(i)
        if chain_len > longest:
            longest = chain_len
            longest_i = i
            print(i,":",chain_len)
        else:
            print(i,":",chain_len,end='\r')

    print(f"Longest chain starts at {longest_i}, with chain length {longest}")
    #print("837799: generate chain",max(generate_chain(837799)))
    #print(collatz)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    now = datetime.now()
    print()
    print("Last ran:", now.strftime("%H:%M"))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.6f} seconds")
