from __future__ import annotations

import lab3


def test_check_sign():
    """
    +----------------------+--------+
    | Input: (params x, y) | Output |
    +----------------------+--------+
    | -1, 1                | True   |
    | 1, -1                | True   |
    | 1, 1                 | False  |
    | -1, -1               | False  |
    +----------------------+--------+
    """
    assert lab3.check_sign(-1, 1) is True
    assert lab3.check_sign(1, -1) is True
    assert lab3.check_sign(1, 1) is False
    assert lab3.check_sign(-1, -1) is False


def test_check_equal():
    """
    +----------------------+--------+
    | Input: (params x, y) | Output |
    +----------------------+--------+
    |                 1, 1 | True   |
    |                 1, 0 | False  |
    +----------------------+--------+
    """
    assert lab3.check_equal(1, 1) is True
    assert lab3.check_equal(1, 0) is False


def test_longest_cond_subseq():
    """
    +----------------------------+--------+
    | Input: (params seq, check) | Output |
    +----------------------------+--------+
    | [], check_sign             |   0, 0 |
    | [1, -1, 1, -1], check_sign |   0, 4 |
    | [1, 1, -1], check_sign     |   1, 2 |
    | [1, 1, 1, 1], check_sign   |   3, 1 |
    | [], check_equal            |   0, 0 |
    | [1, 1, 1, 1], check_equal  |   0, 4 |
    | [1, 2, 2], check_equal     |   1, 2 |
    | [1, 2, 3, 4], check_equal  |   3, 1 |
    +----------------------------+--------+
    """
    seq = []
    assert lab3.longest_cond_subseq(seq, lab3.check_sign) == (0, 0)

    seq = [1, -1, 1, -1]
    assert lab3.longest_cond_subseq(seq, lab3.check_sign) == (0, 4)

    seq = [1, 1, -1]
    assert lab3.longest_cond_subseq(seq, lab3.check_sign) == (1, 2)

    seq = [1, 1, 1, 1]
    assert lab3.longest_cond_subseq(seq, lab3.check_sign) == (3, 1)

    seq = []
    assert lab3.longest_cond_subseq(seq, lab3.check_equal) == (0, 0)

    seq = [1, 1, 1, 1]
    assert lab3.longest_cond_subseq(seq, lab3.check_equal) == (0, 4)

    seq = [1, 2, 2]
    assert lab3.longest_cond_subseq(seq, lab3.check_equal) == (1, 2)

    seq = [1, 2, 3, 4]
    assert lab3.longest_cond_subseq(seq, lab3.check_equal) == (3, 1)


def test_longest_sum_subseq():
    """
    +---------------------+---------------------+
    | Input: (params seq) |       Output        |
    +---------------------+---------------------+
    | []                  | [], 0               |
    | [1, 2, -10, 4, 5]   | [4, 5], 9           |
    | [1, 2, 3, 4, 5]     | [1, 2, 3, 4, 5], 15 |
    +---------------------+---------------------+
    """
    seq = []
    assert lab3.longest_sum_subseq(seq) == ([], 0)

    seq = [1, 2, -10, 4, 5]
    assert lab3.longest_sum_subseq(seq) == (seq[-2:], 9)

    seq = [1, 2, 3, 4, 5]
    assert lab3.longest_sum_subseq(seq) == (seq, 15)
