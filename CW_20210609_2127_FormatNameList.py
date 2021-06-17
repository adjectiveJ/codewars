"""
Codewars - Format a string of names
Author: Dante Valentine
Date: 9 June, 2021
"""


def namelist(names):
    namestring = ""
    for n in names:
        namestring += n['name']
        if names.index(n) == len(names)-2:
            namestring += " & "
        elif names.index(n) < len(names)-1:
            namestring += ", "
    return namestring
        

nameprint = namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
# Bart, Lisa, Maggie, Homer & Marge

print(nameprint)