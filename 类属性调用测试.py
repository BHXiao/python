#!/usr/bin/env python
# -*- coding: utf-8

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

e = Employee("高老大", 28)
print(e.name)
print(e.age)
