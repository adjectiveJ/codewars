"""
Codewars - StringOrder
Author: Dante Valentine
Date: 9 June, 2021
"""

# def order(sent):
#     ordstring = ""
#     ordlist = []
#     slist = sent.split(" ")
#     for i in slist:
#         ordlist.append("")
#     for i in slist:
#         for c in i:
#             if c in "0123456789":
#                 ordlist[int(c)-1] = i
#     ordstring = " ".join(ordlist)
#     return ordstring

def order(sent):
    ordstring = ""
    ordlist = []
    slist = sent.split(" ")
    for i in range(1,10):
        for word in slist:
            if str(i) in word:
                ordlist.append(word)
    ordstring = " ".join(ordlist)
    return ordstring

print(order("is2 Thi1s T4est 3a"))