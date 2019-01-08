o=list(input())
for i in range(0,len(l)-1,2):
    o[i],o[i+1]=o[i+1],o[i]
print("".join(str(x) for x in o))
