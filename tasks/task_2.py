#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from find_min_package import find_min


def main():
    items = ["apple", "banana", "cherry", "date"]
    min_item = find_min(items)
    print(f"Минимальный элемент в списке: {min_item}")

    items_numbers = [42, 17, 23, 8, 15]
    min_number = find_min(items_numbers)
    print(f"Минимальное число в списке: {min_number}")

    items_floats = [3.14, 2.71, 1.41, 1.73]
    min_float = find_min(items_floats)
    print(f"Минимальное число с плавающей точкой в списке: {min_float}")

    items_mixed = [5, 3.5, 2, 4.8]
    min_mixed = find_min(items_mixed)
    print(f"Минимальный элемент в смешанном списке: {min_mixed}")


if __name__ == "__main__":
    main()
