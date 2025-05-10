print("Hello, World, I am back")

total = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i#print(i)
        
print(total)

print("This time I will use inline generator expression")
print(sum(i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0))

print("Trying a math formula solution too")

# Sum of arithmetic sequence 
# n + 2n + 3n + ... + pn
# = n(1 + 2 + 3 + ... + p)
# = np(p+1)/2
def sum_arith_series(n, p):
    return n * p * (p+1) / 2

#print("1+2+3+...+10")
#print(sum_arith_series(1,10))
#
#print("2+4+6+8+10+12")
#print(sum_arith_series(2,6))
#
#print("3+6+9+12")
#print(sum_arith_series(3,4))
#
#print("5+10+15+20+25+30")
#print(sum_arith_series(5,6))


print(sum_arith_series(3,999//3)+sum_arith_series(5,999//5)-sum_arith_series(15,999//15))




