k=int(input("enter the no"))
for j in range(1,k+1):
    if(k%j==0):
        print(j,end=',')
    else:
        print("invalid")
