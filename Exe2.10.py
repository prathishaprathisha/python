m1,m2=input().split(' ')
n=0
for i in range(len(s1)):
    if m1[i]!=m2[i]:
        n=n+1
if(n==1):print('yes')
else:print('no')
