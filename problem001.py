print("Hello, World, I am back")

total = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i#print(i)
        
print(total)

print("This time I will use inline generator expression")
print(sum(i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0))


