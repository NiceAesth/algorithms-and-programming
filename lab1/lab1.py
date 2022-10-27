"""
print("hello!")

numar = 15
numar2 = 16
numar3 = "2"
litera = 'a'
vector = ["a", "b", "c"]

suma = numar + int(numar3)
print(suma)

if numar == 15:
    print("da")
else:
    print("nu")

for i in vector:
    print(i)

for i in range(len(vector)):
    print(vector[i])

for i in range(10):
    print(i)

i = 0
while i < 10:
    print(f"i: {i}")
    i = i+1
"""
"""
x = int(input("Introduceti numarul: "))
x = x + 1
print(x)
"""
from __future__ import annotations


def ex_1():
    suma = 0
    n = int(input("Introduceti n: "))
    for _ in range(n):
        suma += int(input())

    print(f"Suma este: {suma}")


def ex_2():
    prim = True
    x = int(input("Introduceti x: "))
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            prim = False

    print(f"Numarul {x}{' ' if prim else ' nu'} este prim")


def ex_3():
    n = int(input("n: "))
    m = int(input("m: "))
    while m != 0:
        n, m = m, n % m

    print(f"cmmdc: {n}")


if __name__ == "__main__":
    ex_3()
