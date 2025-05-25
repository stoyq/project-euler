def proper_divisors(n):
    if n == 0:
        return []
    if n == 1:
        return [1]

    f = []
    for i in range(1,n):
        if n % i == 0:
            f.append(i)
    return f


# sum of proper divisors of n
def d(n):
    return sum(proper_divisors(n))

print(f"d(28) is {d(28)}")


# calculate all d(n)
D = [] # deficient numbers
P = [] # perfect numbers
A = [] # abundant numbers
Q = [] # for quick recalls
for i in range(28123):
    print("Determining",i,end='\r')
    kind = d(i)
    if kind < i:
        Q.append('deficient')
        D.append(i)
    elif kind == i:
        Q.append('perfect')
        P.append(i)
    else:
        Q.append('abundant')
        A.append(i)
print()
print("There are",len(A),"abundant numbers")

# all possible abundant pair sums
add2 = []
for i in range(len(A)):
    print("i :",i,end='\r')
    for j in range(i, len(A)):
        #if not A[i]+A[j] in add2:
        add2.append(A[i]+A[j])
        #print(A[i]+A[j],"=",A[i],"+",A[j])

print("add1 length:",len(add2))
unique_add2 = list(set(add2))
unique_add2.sort()
print("uniques length:", len(unique_add2))

total = 0
for num in range(1, 28124):
    print("checking num:", num, end='\r')
    if not num in unique_add2:
        total += num
print()
print("total:", total)
