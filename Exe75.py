h = input("Enter String: ")
if len(h) % 2 == 0:

   print(h[len(h) // 2 - 1] + h[len(h) // 2])
   k=h.replace( h[len(h) // 2 - 1],"*")
   print(k.replace(h[len(h) // 2 ],"*"))

else:

   print(h.replace(h[len(h) // 2],"*"))
