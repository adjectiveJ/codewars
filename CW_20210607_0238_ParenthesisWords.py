"""
CodeWars - Duplicate Characters
Author: Dante Valentine
Date: 7 June, 2021
"""


def duplicate_encode(word):
    word = word.lower()
    para = ""
    for c in word:
        count = 0
        for d in word:
            if c == d:
                count += 1
        if count > 1:
            para += ")"
        else:
            para += "("
    return para

word = str(input("Word: "))
paraword = duplicate_encode(word)
print(paraword)