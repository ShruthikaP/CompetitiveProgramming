import unittest
def function(score_list, n):
    count = {}
    for j in score_list:
        s = count.get(j, 0)
        count[j] = s + 1
    ans = []
    for i in range(n + 1):
        if i in count:
            y =[i]*count[i]
            ans.extend(y)
    ans.reverse()
    print("Scores %s sorted list: %s" % (score_list, ans))
    return ans