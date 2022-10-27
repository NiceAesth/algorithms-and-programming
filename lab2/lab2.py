# Ex 2
from __future__ import annotations


def tema_ex_2():
    import datetime

    date_fmt = "%d/%m/%Y"
    date_str = input(f"Enter the date ({date_fmt}): ")
    date = datetime.datetime.strptime(date_str, date_fmt)

    now = datetime.datetime.utcnow()

    delta = now - date
    print(delta.days)


# Ex 10
def tema_ex_10():
    x = input("x: ")
    x_digits = list(x)
    x_digits.sort()

    for i, n in enumerate(x_digits):
        if n != "0":
            first = x_digits.pop(i)
            break

    result_str = first + "".join(x_digits)
    result = int(result_str)
    print(result)


if __name__ == "__main__":
    tema_ex_2()
    tema_ex_10()
