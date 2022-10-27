# Sa se calculeze secventa de lungime maxima care contine doar numere pare
# Sa se calculeze secventa de lungime maxima in care ultima cifra este egala cu 7
from __future__ import annotations

from typing import Callable


def longest_condition_subseq(seq: list, check: Callable):
    check_arr = []
    max_len, max_pos = 0, 0
    for i, x in enumerate(seq):
        if check(x):
            try:
                val = check_arr[i - 1] + 1
                check_arr.append(val)
            except IndexError:
                check_arr.append(1)
        else:
            check_arr.append(0)
        if check_arr[i] >= max_len:
            max_len = check_arr[i]
            max_pos = i - max_len + 1
    return max_pos, max_len


def main():
    def check_even(x: int):
        return x % 2 == 0

    def check_end(x: int):
        return x % 10 == 7

    seq = [1, 2, 2, 3, 2, 2, 2, 4, 5]
    print(longest_condition_subseq(seq, check_even))

    print(longest_condition_subseq(seq, check_end))


if __name__ == "__main__":
    main()
