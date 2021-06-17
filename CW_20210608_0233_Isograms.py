"""
Codewars - Isograms
Author: Dante Valentine
Date: 8 June, 2021
"""

# def is_isogram(string):
#     print(string)
#     string = string.lower()
#     iso = True
#     for c in string:
#         count = 0
#         for d in string:
#             if c == d:
#                 count += 1
#         if count > 1:
#             iso = False
#             # break
#     print(str(iso))
#     return iso

# iso = is_isogram("aba")
# iso = is_isogram("isogram")



def is_isogram(string):
    string = string.lower()
    print(string)
    for c in string:
        if string.count(c) > 1:
            print(c)
            print(string.count(c))
            return False
    return True
    
# iso = is_isogram("aba")
# print(iso)
iso = is_isogram("isogram")
print(iso)