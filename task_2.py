from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge_two_lists(l1, l2))
        lists = merged_lists

    return lists[0]


def merge_two_lists(l1: List[int], l2: List[int]) -> List[int]:
    merged: List[int] = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    merged.extend(l1[i:])
    merged.extend(l2[j:])
    return merged


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6], [9, 10]]
    merged_list = merge_k_lists(lists)
    print("Sorted list:", merged_list)
