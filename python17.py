z=int(input("Enter any number: "))
s=list(map(int,str(n)))
j=list(map(lambda x:x**3,s))
if(sum(j)==z):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
