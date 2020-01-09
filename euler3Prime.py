
def PrimeFactors(x):
    i = 2
    factors = []
    while i*i<=x:
        if x % i:
            i += 1
        else:
            x /= i
            factors.append(i)
    factors.append(int(x))
    return factors


final = PrimeFactors(600851475143)
print(final)