#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Optional


def find_user_id(name: str) -> Optional[int]:
    user = {"Alice": 1, "Bob": 2, "Charlie": 3}
    return user.get(name)


print(find_user_id.__annotations__)
