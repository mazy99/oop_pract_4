#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import List, TypeVar

T = TypeVar("T")


def first(items: List[T]) -> T:
    return items[0]
