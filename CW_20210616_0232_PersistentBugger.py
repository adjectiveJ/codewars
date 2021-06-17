"""
CodeWars - Persistent Bugger
Author: Dante Valentine
Date: 16 June, 2021
"""

# def persistence(n):
#     m = n
#     count = 0
#     while m > 9:
#         count += 1
#         o = 1
#         for i in str(m):
#             o *= int(i)
#         m = o
#     return count


def persistence(n):
    count = 0
    while n > 9:
        count += 1
        o = 1
        for i in str(n):
            o *= int(i)
        n = o
    return count

print(persistence(999))