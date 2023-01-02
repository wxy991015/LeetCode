#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:48:16 2022

@author: xiaoyangwei
"""

def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    names_heights = dict()
    for i in range(len(names)):
        names_heights[heights[i]] = names[i]
    sorted_names_heights = dict(sorted(names_heights.items(), reverse=True))
    return list(sorted_names_heights.values())

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(f"Output: {sortPeople(names, heights)}")