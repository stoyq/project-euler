S = set()
for a in range(2, 101):
    for b in range(2, 101):
        c = pow(a, b)
        S.add(c)

print(len(S))
