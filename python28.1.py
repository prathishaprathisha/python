 
def linearSearch(a, d): 
    for i in range(d): 
        if a[i] is i: 
            return i 
    return -1

a = [-10, -1, 0, 3, 10, 11, 30, 50, 100] 
d = len(a) 
print("Fixed Point is " + str(linearSearch(arr,n)))
