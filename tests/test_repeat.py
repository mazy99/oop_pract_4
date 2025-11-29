#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import get_type_hints

from tasks.repeat import repeat


def test_type_hints_exist():
    hints = get_type_hints(repeat)
    assert "s" in hints
    assert "n" in hints
    assert "return" in hints


def test_type_hints_correct():
    hints = get_type_hints(repeat)
    assert hints["s"] == str
    assert hints["n"] == int
    assert hints["return"] == str


def test_repeat_correctness():
    assert repeat("abc", 3) == "abcabcabc"
    assert repeat("", 5) == ""
    assert repeat("x", 0) == ""
    assert repeat("test", 1) == "test"


def test_argument_types():
    hints = get_type_hints(repeat)
    s_val = "Hello"
    n_val = 3
    result = repeat(s_val, n_val)
    assert isinstance(result, hints["return"])
    assert isinstance(n_val, hints["n"])
    assert isinstance(s_val, hints["s"])
