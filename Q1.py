list = ['cbc', 'xyz', 'abb', '1221']
count = 0
for check in list:
    if len(check) >= 2:
        if check[0] == check[len(check)-1]:
            count = count+1
print(count)
