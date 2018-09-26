SECONDS_PER_a  = 60
SECONDS_PER_b    = 3600
SECONDS_PER_c    = 86400
c   = int(input("Enter number of Days: "))
b  = int(input("Enter number of Hours: "))
a= int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))
total_seconds = days * SECONDS_PER_DAY
total_seconds = total_seconds + ( hours * SECONDS_PER_HOUR)
total_seconds = total_seconds + ( minutes * SECONDS_PER_MINUTE)
total_seconds = total_seconds + seconds
print("Total number of seconds: ","%d"%(total_seconds))
