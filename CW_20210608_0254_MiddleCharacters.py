"""
Codewars - Middle Characters
Author: Dante Valentine
Date: 8 June, 2021
"""

def get_middle(s):
    midindex = int(len(s)/2)
    if len(s) % 2 > 0:
        return s[midindex]
    else:
        return s[(midindex-1):midindex+1]

words = ["cat", "house", "pancake", "grades"]
for e in words:
    f = get_middle(e)
    print(e, f)