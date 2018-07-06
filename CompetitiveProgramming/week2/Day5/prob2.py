import unittest
def function(num_list):
    if len(num_list) < 2:
        raise ValueError('Atleast two numbers required')
    n = len(num_list) - 1
    ans= (n * n + n) / 2
    actual_sum = sum(num_list)
    return actual_sum - ans