import random
nt = ()
for c in range(0, 6):
    e = random.randint(1, 20)
    nt = tuple(list(nt) + [e])
print(nt)
print(min(nt))
print(max(nt))