def char_frequency(str1):
    dict = {}
    for m in str1:
        keys = dict.keys()
        if  m in keys:
            dict[m] += 1
        else:
            dict[m] = 1
    return dict
print(char_frequency('google.com'))
