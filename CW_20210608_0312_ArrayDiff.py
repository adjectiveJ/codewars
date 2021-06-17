"""
Codewars - Array differences
Author: Dante Valentine
Date: 8 June, 2021
"""

# def array_diff(a, b):
#     for iB in b:
#         for iA in a:
#             if a.count(iB) > 0:
#                 a.remove(iB)
#     return a


def array_diff(a, b):
    for i in b:
        while a.count(i) > 0:
            a.remove(i)
    return a
print(array_diff([1,2,3,4,5,12,4,1,2],[2,4]))