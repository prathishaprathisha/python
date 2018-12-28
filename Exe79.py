c=int(input("enter the no"))
d=int(input("enter the no"))
flag=0
e=c*d

for i in range(0,e+1):
    if(i**2==e):
      flag=flag+1


if(flag==1):
    print("yes")
else:
    print("no")
