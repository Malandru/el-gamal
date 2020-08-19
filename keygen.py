import primes
import random


class Keygen:
    def __init__(self):
        a, b = pow(10, 20), pow(10, 50)
        p = primes.generate_big_prime(a, b, 5)
        g = gcg(p)

        x = random.randint(2, p)
        y = pow(g, x, p)
        self.public_key = (p, g, y)
        self.private_key = x


def gcg(p):  # generator of cyclic group
    g = random.randint(2, p)
    while gcd(p, g) != 1:
        g = random.randint(2, p)
    return g


def gcd(a, b):
    if a < b:
        return gcd(a, b)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    keygen = Keygen()
    print(keygen.public_key)
    print(keygen.private_key)
