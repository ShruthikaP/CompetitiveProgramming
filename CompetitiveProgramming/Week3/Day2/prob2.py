import unittest
def find_repeat(lis):
    a=1
    b=len(lis)-1
    while a<b:
        midpoint=a+((b-a)/2)
        lrange_a, lrange_b=a,midpoint
        urange_a,urange_b= midpoint+1,b
        c=0
        for i in lis:
            if i>=lrange_a and i<=lrange_b:
                c+= 1
        d=(lrange_b-lrange_a+1)
        if c>d:
            a,b=lrange_a,lrange_b
        else:
            a,b=urange_a,urange_b
    return a