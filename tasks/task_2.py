#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from find_min_package import find_min


def main():
    items = ["apple", "banana", "cherry", "date"]
    min_item = find_min(items)
    print(f"Минимальный элемент в списке: {min_item}")


if __name__ == "__main__":
    main()
