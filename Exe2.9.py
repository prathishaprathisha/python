lo,up=map(int,input().split(' '))
k=list(1 for i in range(up+1))
s=0
for i in range(2,up+1,1):
    if k[i]==1:
        for j in range(i*i,up+1,i):
            k[j]=0
        if i>=lo:
            s+=1
print(s)
