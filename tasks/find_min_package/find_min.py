#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import List, Protocol, TypeVar


class AnyComparableClass(Protocol):
    def __lt__(self, other: AnyComparableClass) -> bool: ...


T = TypeVar("T", bound=AnyComparableClass)


def find_min(items: List[T]) -> T:
    if items:
        return min(items)
    raise ValueError("Список не должен быть пустым")


def main():
    items = ["apple", "banana", "cherry", "date"]
    min_item = find_min(items)
    print(f"Минимальный элемент в списке: {min_item}")


if __name__ == "__main__":
    main()
