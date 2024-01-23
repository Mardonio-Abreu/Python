list = range(9, 99, 1)

for i in list:
    if (((i-2)%3 == 0) and ((i-3)%4 == 0) and ((i-4)%5 == 0)):
        print(i)