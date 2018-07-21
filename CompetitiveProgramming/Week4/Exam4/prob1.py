def con_ones(n):
    count = 0
    while (n!=0):
        n = (n & (n << 1))
        count=count+1
    return count
num=int(input())
print(con_ones(num))
