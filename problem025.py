# starting Fibonacci numbers
F_prev = 1
F_next = 1
index_next = 2
n_digits = 1 

while n_digits < 1000:
    n_digits = len(str(F_next))
    print(f"F({index_next}) has {n_digits} digits")
    temp = F_prev
    F_prev = F_next
    F_next = temp + F_next
    index_next += 1

