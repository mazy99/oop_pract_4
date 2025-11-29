#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Union


def normalize(value: Union[int, float, str]) -> float:
    if isinstance(value, str):
        value = value.replace(",", ".")
        return float(value)
    return float(value)


print(normalize.__annotations__)
