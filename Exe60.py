m=int(input("Enter Fibonacci Range"))
m1 = 0
m2 = 1
count = 0
l=[]
if n == 1:
    l.append(m1)
else:
    while count < m:
        l.append(n1)
        mth = m1 + m2
        m1 = m2
        m2 = mth
        count += 1
print(" ".join(str(y) for y in l))
