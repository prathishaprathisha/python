p=int(input("enter a number:"))
rv=0
if(p>0):
    while p>0:
        rm=n%10
        rv=rv*10+rm
        n=n//10
    print("the number is:",rv)
else:
    print "invalid"
