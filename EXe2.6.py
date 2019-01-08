st1,st2=map(str,input().split())
y=list(st1)
o=list(st2)
for x in range(len(a)-1):
	flag=0
	for y in range(x+1,len(y)):
		if (y[x]==y[y]):
			y[y]='*'
			flag=1
	if flag==1:
		y[x]='*'
	elif(flag==0) and y[x]!='*':
		y[x]='#'
for x in range(len(o)-1):
	flag=0
	for y in range(x+1,len(o)):
		if o[x]==o[y]:
			o[y]='*'
			flag=1
	if flag==1:
		o[x]='*'
	elif(flag==0) and o[x]!='*':
		o[x]='#'
if(y[len(y)-1]!='*'):
	y[len(y)-1]='#'
if(y[len(y)-1]!='*'):
	y[len(y)-1]='#'
ans1=''
ans2=''
for x in y:
	ans1=ans1+x
for x in o:
	ans2=ans2+x
if(ans1==ans2):
	print("yes")
else:
	print("no")
