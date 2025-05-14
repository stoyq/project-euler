import time

print("--- Method 1 ---")
start = time.perf_counter()
# brute force first
for a in range(1,1000):
    for b in range(a+1,1000):
        for c in range(b+1,1000):
            if a + b + c != 1000:
                continue
            
            if a*a + b*b == c*c:
                print(a,"+",b,"+",c,"=",a+b+c)
                print(a,"*",b,"*",c,"=",a*b*c)

end = time.perf_counter()

print(f"Elapsed time: {end - start:.6f} seconds")



print("--- Method 2 ---")
start = time.perf_counter()
# reduce to 2 loops only by calculating c
for a in range(1,1000):
    for b in range(a+1,1000):
        c = 1000 - a -b
        
        if a*a + b*b == c*c:
            print(a,"+",b,"+",c,"=",a+b+c)
            print(a,"*",b,"*",c,"=",a*b*c)

end = time.perf_counter()
print(f"Elapsed time: {end - start:.6f} seconds")
