# 11, 12
from __future__ import annotations
import os
from typing import Callable


def check_sign(x: int, y: int) -> bool:
    """Check if two integers have opposite signs
    x, y - integers
    Returns True if elements have opposite signs, False otherwise
    """
    return (x <= 0) != (y <= 0)


def check_equal(x: int, y: int) -> bool:
    """Check if two integers are equal
    x, y - integers
    Return bool - True if elements are equal, False otherwise"""
    return x == y


def longest_cond_subseq(seq: list, check: Callable) -> "(int, int)":
    """Finds the longest subsequence that respects a given check.
    seq - list
    check - Callable(x, y) -> bool, function to check adjacent elements
    Return (max_pos, max_len) - Start position of the subsequence, length of the subsequence
    """
    n = len(seq)

    check_arr = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if check(seq[i], seq[j]) and check_arr[i] < check_arr[j] + 1:
                check_arr[i] = check_arr[j] + 1

    max_pos, max_len = 0, 0

    for i in range(n):
        if max_len <= check_arr[i]:
            max_len = check_arr[i]
            max_pos = i - max_len + 1

    return max_pos, max_len


def longest_sum_subseq(seq) -> "(list, int)":
    """Finds the longest subsequence of the maximum size.
    seq - list
    Return (subseq, max_len) - List containing the subsequence elements, sum of the subseq elements
    """
    best, curr = 0, 0
    curr_start, start, end = 0, 0, 0
    for i, x in enumerate(seq):
        if curr + x > 0:
            curr += x
        else:
            curr, curr_start = 0, i + 1

        if curr > best:
            start, end, best = curr_start, i + 1, curr
    return seq[start:end], best


def clear() -> None:
    """Clears the terminal.
    Clears the terminal based on the host OS.
    Return NoneType
    """
    os.system("cls" if os.name == "nt" else "clear")


def read() -> list:
    """Reads a list of n integers from the terminal.
    n - int
    list[i] - int
    Return list - List of integers read
    """
    n = int(input("Length of list: "))
    return [int(input()) for _ in range(n)]


def main() -> None:
    """Menu function of the app.
    Return NoneType
    """
    seq = []
    while True:
        options = {
            1: "Input the array of numbers",
            2: "Get the longest sub-array with the maximum sum",
            3: "Get the longest sub-array with opposite sign neighbors",
            4: "Get the longest sub-array with equal elements",
            5: "Exit",
        }  # List of menu item classes could be implemented (would hold option msg and callable object)
        # Would remove the need for ifs
        clear()
        print(options)
        opt = int(input("Enter your selection: "))
        if opt == 1:
            seq = read()
        elif opt == 2:
            subseq, res = longest_sum_subseq(seq)
            print(f"Subsequence: {subseq}, Sum of: {res}")
            input("Press any key to continue...")
        elif opt == 3:
            start, length = longest_cond_subseq(seq, check_sign)
            print(f"Starts on: {start}, Length of: {length}")
            input("Press any key to continue...")
        elif opt == 4:
            start, length = longest_cond_subseq(seq, check_equal)
            print(f"Starts on: {start}, Length of: {length}")
            input("Press any key to continue...")
        elif opt == 5:
            exit()
        else:
            input("Invalid selection.")


if __name__ == "__main__":
    main()
