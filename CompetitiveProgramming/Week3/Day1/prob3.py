import random
def rand5():
    return random.randrange(1, 6)

def rand7():
    while True:
        n1 = 5 * (rand5() - 1)
        n2 = rand5()
        n = n1 + n2
        if n <= 21:
            return n % 7 + 1
print rand7()