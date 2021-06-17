"""
CodeWars - Detect Pangram
Author: Dante Valentine
Date: 16 June, 2021
"""

import string

def is_pangram(s):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in s.lower():
            return False
    return True