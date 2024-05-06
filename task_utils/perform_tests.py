import pandas as pd
from threading import Thread
import timeit
from typing import Any, Callable, Dict, List, Union

from task_utils.sort_implementation import insertion_sort, merge_sort, tim_sort


def get_sort_time(sort_func: Callable, arr: List[Any]) -> float:
    return timeit.timeit(lambda: sort_func(arr), number=1)


def test_sort(sort_func: Callable, array: List[Any], array_type: str = "Unsorted") -> Dict[str, Union[str, int, float]]:
    if array_type.lower() not in ["sorted", "unsorted", "reversed"]:
        raise ValueError("Invalid array type. Choose from 'sorted', 'unsorted', 'reversed'.")
    results = {
        "Array Type": array_type,
        "Algorithm": sort_func.__name__ if sort_func not in ["sort", sorted] else "Built-in TimSort",
        "Time": get_sort_time(sort_func, array.copy()),
        "Array Size": len(array),
    }
    return results


def run_reverse_tests(res: list, runs_number: int = 1, start: int = 1000, stop: int = 10001, step: int = 1000) -> list:
    for _ in range(runs_number):
        for i in range(start, stop, step):
            arr = list(range(i, 0, -1))
            for call in [insertion_sort, merge_sort, sorted, tim_sort]:
                t = Thread(target=res.append, args=(test_sort(call, arr, "Reversed"),))
                t.start()
                t.join()
    return res


def run_unsorted_tests(res: list, runs_number: int = 1, start: int = 1000, stop: int = 10001, step: int = 1000) -> list:
    import random

    for _ in range(runs_number):
        for i in range(start, stop, step):
            arr = [random.randint(1, 100) for _ in range(i)]
            for call in [insertion_sort, merge_sort, sorted, tim_sort]:
                t = Thread(target=res.append, args=(test_sort(call, arr, "Unsorted"),))
                t.start()
                t.join()
    return res


def run_sorted_tests(res: list, runs_number: int = 1, start: int = 1000, stop: int = 10001, step: int = 1000) -> list:
    for _ in range(runs_number):
        for i in range(start, stop, step):
            arr = list(range(1, i))
            for call in [insertion_sort, merge_sort, sorted, tim_sort]:
                t = Thread(target=res.append, args=(test_sort(call, arr, "Sorted"),))
                t.start()
                t.join()
    return res


def run_tests(res: pd.DataFrame,
              arr_types: List[str],
              runs_number: int = 3,
              start: int = 1000,
              stop: int = 10001,
              step: int = 1000
              ) -> pd.DataFrame:
    results = []
    for arr_type in arr_types:
        if arr_type.lower() == "reversed":
            t = Thread(target=run_reverse_tests, args=(results, runs_number, start, stop, step))
        elif arr_type.lower() == "unsorted":
            t = Thread(target=run_unsorted_tests, args=(results, runs_number, start, stop, step))
        elif arr_type.lower() == "sorted":
            t = Thread(target=run_sorted_tests, args=(results, runs_number, start, stop, step))
        else:
            raise ValueError("Invalid array type. Choose from 'sorted', 'unsorted', 'reversed'.")
        t.start()
        t.join()

    res = pd.concat([pd.DataFrame(results), res])
    return res

