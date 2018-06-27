def making_change(amt, p):
    change = [0] * (amt + 1)
    change[0] = 1
    for i in p:
        for x in xrange(i, amt + 1):
            rem = x - i
            change[x] += (change[rem])
    return change[amt]