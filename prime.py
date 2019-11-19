primes = [2]
i = 3
while len(primes) < 100:
    for p in primes:
        if (i % p == 0) or (p*p > i):
            break

    if i%p != 0:
        primes.append(i)
        print(i)
    i = i + 2    # Why is it 2 instead of 1.
