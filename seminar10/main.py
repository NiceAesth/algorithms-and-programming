from __future__ import annotations


def recursive_search(data, target):
    if len(data) == 0:
        return False
    if data[0] == target:
        return True
    return recursive_search(data[1:], target)


def recursive_binary_search(data, target):
    if len(data) == 0:
        return False
    mid = len(data) // 2
    if data[mid] == target:
        return True
    if data[mid] > target:
        return recursive_binary_search(data[:mid], target)
    return recursive_binary_search(data[mid + 1 :], target)


def recursive_exponential_search(data, target):
    if data[0] == target:
        return True

    i = 1
    while i < len(data) and data[i] <= target:
        i *= 2

    return recursive_binary_search(data[i // 2 : min(i, len(data))], target)


def select_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


def insertion_sort(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j - 1] > data[j]:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
    return data


def bubble_sort(data):
    ok = True
    while ok:
        ok = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                ok = True
    return data


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(recursive_search(data, 5))
    print(recursive_search(data, 11))
    print(recursive_binary_search(data, 5))
    print(recursive_binary_search(data, 11))
    print(recursive_exponential_search(data, 5))
    print(recursive_exponential_search(data, 11))
    print(select_sort(new_data))
    print(insertion_sort(new_data))
    print(bubble_sort(new_data))
