#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


BoxInt = Box[int](123)
BoxStr = Box[str]("Hello")
print(BoxInt.get())  # Output: 123
print(BoxStr.get())  # Output: Hello
