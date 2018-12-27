m=input("Enter Alphanumeric")
a=0
b=0
for char in m:
    if(char.isdigit()):a=a+1
    if(char.isalpha()):b=b+1
    if(a>0 and b>0):
        print('yes')
        break
if(a==0 or b==0):print('No')
