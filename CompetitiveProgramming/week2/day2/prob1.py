import unittest
def get_closing_paren(s, pos):
    i = pos
    n = len(s)
    count = 0
    while i < n:
        c = s[i]
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
            if count == 0:
                return i
        i += 1
    if count!=0:
        raise Exception