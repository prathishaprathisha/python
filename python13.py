t = int(input("Enter any number: "))
if t > 1:
    for i in range(2, t):
        if (t % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
