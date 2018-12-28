d=input("calculator")
try:
  k=d.split("/")
  print(int(k[0])/int(k[1]))
except:
    k = d.split("%")
    print(int(k[0])%int(k[1]))
