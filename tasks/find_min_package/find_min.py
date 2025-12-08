#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Protocol, TypeVar


class AnyComparableClass(Protocol):
    def __lt__(self, other: AnyComparableClass) -> bool: ...


T = TypeVar("T", bound=AnyComparableClass)


def find_min(items: list[T]) -> T:
    if items:
        return min(items)
    raise ValueError("Список не должен быть пустым")
