def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
primes = []
with open('primes-to-100k.txt') as my_file:
    primes = my_file.read().splitlines()
i = 0
for prime in primes:
    equation = ((3 * int(prime))) - 10
    if not str(equation) in primes:
        print("\rNope: {}".format(prime))
        print("\rOutput: {}".format(equation))
        print("\rFactored: {}".format(prime_factors(equation)))
        i += 1
        if (i == 200):
            exit()
    else:
        print("Skipped:{}".format(prime))
