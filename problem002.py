# First two terms of the Fib sequence
a = 1
b = 2
total = 0

while b < 4000000:
    # add only the even terms
    if b % 2 == 0:
        print(b, "added")
        total = total + b

    # calculate next Fib term
    c = a + b

    # update a and b
    a = b
    b = c
    #print(c)

print("total:", total)
