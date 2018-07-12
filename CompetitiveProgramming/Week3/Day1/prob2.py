import random
def rand7():
    return random.randrange(1, 8)

def rand5():
    while True:
        n = rand7()
        if n < 6:
            return n
print rand5()