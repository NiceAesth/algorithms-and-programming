from __future__ import annotations


def len_recursive(lst):
    if not lst:
        return 0
    return 1 + len_recursive(lst[1:])


def remove_last_recursive(lst):
    if len(lst) == 1:
        return []
    return [lst[0]] + remove_last_recursive(lst[1:])


def get_last_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return get_last_recursive(lst[1:])


def add_last_recursive(lst, element):
    if not lst:
        return [element]
    return [lst[0]] + add_last_recursive(lst[1:], element)


def check_odd_length_recursive(lst):
    if len(lst) == 1:
        return True
    if len(lst) == 2:
        return False
    return check_odd_length_recursive(lst[2:])


def check_odd_length_recursive(lst):
    if len(lst) == 1:
        return False
    if len(lst) == 1:
        return True
    return not check_odd_length_recursive(lst[1:])


def product_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] * product_recursive(lst[1:])


def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)


def power_logarithmic_recursive(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return power_recursive(base * base, exponent // 2)
    return base * power_recursive(base, exponent - 1)


def sum_alternating_sign_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] - sum_alternating_sign_recursive(lst[1:])


if __name__ == "__main__":
    print(len_recursive([1, 2, 3]))
    print(remove_last_recursive([1, 2, 3]))
    print(get_last_recursive([1, 2, 3]))
    print(add_last_recursive([1, 2, 3], 4))
    print(check_odd_length_recursive([1, 2, 3, 4, 5]))
    print(product_recursive([1, 2, 3, 4, 5]))
    print(power_recursive(2, 5))
    print(power_logarithmic_recursive(2, 5))
    print(sum_alternating_sign_recursive([1, 2, 3, 4, 5]))
