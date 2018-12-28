z=input("enter the number")
if(z<=100000000000):
    k=len(z)
    i=0
    f=1
    while i<int(k):
        m=m*int(z[i])
        i+=1
    print(m)
