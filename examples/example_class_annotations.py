#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student:
    name: str
    grades: list[int]

    def __init__(self, name: str, grades: list[int]) -> None:
        self._name = name
        self._grades = grades

    def average(self) -> float:
        return sum(self._grades) / len(self._grades)


print(f"Ожидаемые типы данных для класса Student: {Student.__annotations__}")
print(f"Ожидаемые типы данных для метода __init__: {Student.__init__.__annotations__}")
print(f"Ожидаемые типы данных для метода average: {Student.average.__annotations__}")
