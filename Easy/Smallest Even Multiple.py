#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:20:39 2022

@author: xiaoyangwei
"""

def smallestEvenMultiple(n: int) -> int:
    if n % 2 != 0:
        return 2 * n
    return n

n = 5
print(f"Output: {smallestEvenMultiple(n)}")