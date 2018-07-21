def counting_bits(str):
    count=0
    for i in str:
        if(i=='1'):
            count=count+1
    return count

n=int(input())
str=""
l=[]
for i in range(0,n+1):
    str=bin(i)
    ans=counting_bits(str)
    l.append(ans)
print(l)
