import unittest
def get(s):
    if len(s) <= 1:
        return set([s])
    mid = s[:-1]
    end = s[-1]
    mid_perm = get(mid)
    p = set()
    for i in mid_perm:
        for j in range(len(mid) + 1):
            ans = (i[:j] + end + i[j:])
            p.add(ans)
    return p