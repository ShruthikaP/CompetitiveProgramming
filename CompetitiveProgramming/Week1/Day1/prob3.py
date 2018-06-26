  def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Atleast 3 items required.')
    high = max(list_of_ints[0], list_of_ints[1])
    low  = min(list_of_ints[0], list_of_ints[1])
    hp2 = list_of_ints[0] * list_of_ints[1]
    lp2  = list_of_ints[0] * list_of_ints[1]
    hp3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    for i in xrange(2, len(list_of_ints)):
        c = list_of_ints[i]
        hp3 = max(hp3, c * hp2, c * lp2)
        hp2 = max(hp2, c * high, c * low)
        lp2 = min(lp2, c * high, c * low)
        high = max(high, c)
        low = min(low, c)
    return hp3