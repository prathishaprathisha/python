s,t=map(int,input("Enter Two values").split(' '))
s = s ^ t;
t = s ^ t;
s = s^ t;
print(s,t)
