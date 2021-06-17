"""
CodeWars - Sum of the first nth term of Series
Author: Dante Valentine
Date: 16 June, 2021
"""

# def series_sum(n):
#     denom = 1.00
#     ans = 0.00
#     for i in range(0,n):
#         ans += 1.00/denom
#         denom += 3.00
#         print(ans)
#     return '{:.2f}'.format(ans)

def series_sum(n):
    ans = 0
    for i in range(0,n):
        ans += 1/(1 + 3 * i)
    return '{:.2f}'.format(ans)

print(series_sum(3))