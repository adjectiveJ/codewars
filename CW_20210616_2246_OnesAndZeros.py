"""
CodeWars - Ones And Zeros
Author: Dante Valentine
Date: 16 June, 2021
"""

def binary_array_to_number(arr):
    return int(''.join([str(x) for x in arr]), 2)

print(binary_array_to_number([1,1,1,1]))