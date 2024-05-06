from typing import Any, List


def insertion_sort(arr: List[Any]) -> List[Any]:
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def merge_sort(arr: List[Any]) -> List[Any]:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def tim_sort(arr: List[Any]) -> List[Any]:
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr[i:i + min_run])

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            end = min(n - 1, start + size * 2 - 1)
            merge_sort(arr[start:end + 1])
        size *= 2

    return arr
