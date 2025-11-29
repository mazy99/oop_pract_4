#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


print(f"Типы данных класса Box: {Box.__annotations__}")
print(f"Типы данных метода __init__:{Box.__init__.__annotations__}")
print(f"Типы данных метода get: {Box.get.__annotations__}")
