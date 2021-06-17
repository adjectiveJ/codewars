"""
CodeWars - UniqueInOrder
Author: Dante Valentine
Date: 16 June, 2021
"""

def unique_in_order(iterable):
    newlist = []
    for c, i in enumerate(iterable):
        if c == 0 or i != iterable[c-1]:
            newlist.append(i)
    return newlist

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1,2,2,3,3]))