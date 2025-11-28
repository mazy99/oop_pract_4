#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import get_type_hints

from repeat import repeat


def main():
    s_val = "Hello "
    n_val = 3
    rep = repeat(s_val, n_val)
    func_hints = get_type_hints(repeat)
    actual_s = type(s_val)
    actual_n = type(n_val)
    actual_return = type(rep)
    print(f"\nРезультат вызова функции repeat: {rep}")
    print(f"\nТип аргумента 's': ожидается {func_hints['s']}, получен {actual_s}")
    print(f"\nТип аргумента 'n': ожидается {func_hints['n']}, получен {actual_n}")
    print(
        f"\nТип возвращаемого значения: ожидается {func_hints['return']}\
, получен {actual_return}\n"
    )


if __name__ == "__main__":
    main()
