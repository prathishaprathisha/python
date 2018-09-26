t= float(input("Input time in seconds: "))
day = t
t = t % (24 * 3600)
hour = t 
t %= 3600
minutes = t 
t %= 60

print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, ))
