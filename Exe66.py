def fact(m) :
    if m> 1:
        for i in range(2,m):
            if (m % i) == 0:
                return "no"
        return "yes"
    return "no"
m= int(input(
   "Enter value"))
print(fact(m))
