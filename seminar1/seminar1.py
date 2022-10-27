from __future__ import annotations

from math import sqrt


def check_prime(n: int):
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def next_prime(n: int):
    while True:
        n += 1
        if check_prime(n):
            return n


def next_k_primes(n: int, k: int):
    primes = []
    for _ in range(k):
        n = next_prime(n)
        primes.append(n)
    return primes
