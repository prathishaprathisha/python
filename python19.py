l=7

factorial = 1
if l< 0:
   print("Sorry, factorial does not exist for negative numbers")
elif l == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,l + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
