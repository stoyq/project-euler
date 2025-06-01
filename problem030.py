max_sum = 5 * 9**5

total = 0
for i in range(2,max_sum+1):
    add_up = 0
    for c in str(i):
        add_up += (int(c))**5

    if str(add_up) == str(i):
        print(add_up)
        total += add_up

print("total:", total)

