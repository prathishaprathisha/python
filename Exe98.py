p=int(input("enter th:e n"))
a=[]
for i in range(0,p):
    c=int(input("enter the input"))
    a.append(c)
for i in range(0,p):
    if(a[i]!=i+1):
        print(i+1)
