from collections.abc import Iterable
from datetime import timedelta
from typing import Protocol, runtime_checkable


@runtime_checkable
class Addable(Protocol):
    def __add__(self, other):
        ...


def deep_add(data: Iterable, start: Addable = 0) -> Addable:
    res = start
    for item in data:
        if not isinstance(item, Addable):
            res = deep_add(item, start=res)
            continue
        try:
            res += item
        except TypeError:
            res = deep_add(item, start=res)

    return res


if __name__ == "__main__":
    print(deep_add([1, 2, 3, 4]))  # 10
    print(deep_add([[1, 2, 3], [4, 5, 6]]))  # 21
    print(deep_add([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]))  # 36
    print(deep_add([(1, 2), [3, {4, 5}]]))  # 15
    print(deep_add([[1, 2], [3, 4]], start=2))  # 12
    print(deep_add([[]], start=10))  # 10

    numbers = [1, 2, 3, 4]
    cubes_and_squares = ((n, (n**3, n**2)) for n in numbers)
    print(deep_add(cubes_and_squares))  # 140
    print(deep_add([(1, 2), [3, {4, 5}]]))  # 15
    print(
        deep_add(
            [[timedelta(5), timedelta(10)], [timedelta(3)]], start=timedelta(0)
        )
    )  # datetime.timedelta(days=18)
