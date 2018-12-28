m=int(input("enter  no"))
n=int(input("enter  no"))
for j in range(n,0,-1):
    if(m%j==0 and n%j==0):
      print(j)
      break
