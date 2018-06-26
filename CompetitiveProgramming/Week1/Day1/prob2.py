def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Atleast 2 numbers required')
    products = [None] * len(int_list)
    pdt = 1
    for i in xrange(len(int_list)):
        products[i] = pdt
        pdt *= int_list[i]
    pdt = 1
    for i in xrange(len(int_list) - 1, -1, -1):
        products[i] *= pdt
        pdt *= int_list[i]
    return products