#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:14:49 2022

@author: xiaoyangwei
"""

def convertTemperature(celsius: float) -> list[float]:
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]

celsius = 36.50
print(f"Output: {convertTemperature(celsius)}")