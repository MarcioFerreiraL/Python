import random
while True:
    num = random.randint(-5,20)
    if num < 0:
        break
    print('-' * 15)
    for c in range(1, 11):
        print(f'{num} x {c:>2} = {num * c}')
    print('-' * 15)
