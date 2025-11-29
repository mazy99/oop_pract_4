#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import get_type_hints

import pytest

from tasks.find_min_package.find_min import AnyComparableClass, T, find_min


def test_find_min_type_hints():
    hints = get_type_hints(find_min)
    assert "items" in hints
    assert "return" in hints


def test_find_min_correctness():
    assert find_min([3, 1, 2]) == 1
    assert find_min(["banana", "apple", "cherry"]) == "apple"
    assert find_min([5.5, 2.2, 3.3]) == 2.2


def test_argument_types():
    items_val = [3, 1, 2]
    result = find_min(items_val)
    assert type(result) is type(items_val[0])
    assert isinstance(items_val, list)


def test_typevar_bound():
    assert T.__bound__ is AnyComparableClass


def test_find_min_empty_list():
    with pytest.raises(ValueError):
        find_min([])
