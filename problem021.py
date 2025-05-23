
def proper_divisors(n):
    f = []
    for i in range(1,n):
        if n % i == 0:
            f.append(i)
    return f

#def factors(n):
#    f = []
#    for i in range(1,n+1):
#        if n % i == 0:
#            f.append(i)
#    return f

# sum of proper divisors of n
def d(n):
    return sum(proper_divisors(n))

print(f"d(200) is {d(220)}")
print(f"d(284) is {d(284)}")
print(f"d(9999) is {d(9999)}")


# calculate all d(n)
D = []
for i in range(25400):
    D.append(d(i))

#print(max(D))

# check for amicable pairs
total = 0
for i in range(10000):
    if i == D[D[i]] and i != D[i]:
        print(f"d({i})={D[i]} and d({D[i]})={D[D[i]]}")
        total = total + i

print("total:", total)
