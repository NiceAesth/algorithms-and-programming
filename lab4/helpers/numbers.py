import math
from tabnanny import check

__all__ = ["check_prime"]


def check_prime(x: int):
    if x < 2 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True
