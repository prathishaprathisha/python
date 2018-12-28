def do_stuff(input):
w,p = [int(x) for x in input.split(" ")]
print(p-w)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
