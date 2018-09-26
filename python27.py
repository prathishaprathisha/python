k = 'a123'
try:
    j = float(k)
except (ValueError, TypeError):
    print('\nNot numeric')
print()
