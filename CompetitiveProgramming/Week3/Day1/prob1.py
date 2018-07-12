import unittest
def function(half1, half2, shuffled_deck):
    h1 = 0
    h2 = 0
    for i in shuffled_deck:
        if h1 < len(half1) and i == half1[h1]:
            h1 += 1
        elif h2 < len(half2) and i == half2[h2]:
            h2 += 1
        else:
            return False
    return True