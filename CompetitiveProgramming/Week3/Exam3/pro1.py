i1=int(input())
i2=int(input())
n1=bin(i1)

n2=bin(i2)
x1=n1.split("b")
x2=n2.split("b")
k1=(x1[1])
k2=(x2[1])
k1=k1[::-1]
k2=k2[::-1]
##print(k1,k2)
while(len(k1)!=len(k2)):
    if(len(k1)>len(k2)):
            k2=k2+'0'
    else:
            k1=k1+'0'
##print(k1,k2)
count=0
for i in range(0,len(k1)):
    if(k1[i]!=k2[i]):
        count=count+1
print(count)
