"""
Codewars - Binary Addition
Author: Dante Valentine
Date: 9 June, 2021
"""
# import math as m
# def add_binary(a,b):
#     c = a+b
#     d = bin(c)
#     d = d[2:]
#     return d


# OTHER SOLUTIONS
# def add_binary(a,b):
#     return bin(a+b)[2:]

def add_binary(a,b):
    return "{0:b}".format(a+b)

print(add_binary(51,12))
