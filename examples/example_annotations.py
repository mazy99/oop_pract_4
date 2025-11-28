#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# no type annotations
def total_price_1(price, tax):
    return price + (price * tax)


# with type annotations
def total_price_2(price: float, tax: float) -> float:
    return price + (price * tax)
