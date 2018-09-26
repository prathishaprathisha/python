h=[]
m=int(input("Enter number of elements:"))
for i in range(1,m+1):
    b=input("Enter element:")
    h.append(b)
h.sort(key=len)
print(h)
