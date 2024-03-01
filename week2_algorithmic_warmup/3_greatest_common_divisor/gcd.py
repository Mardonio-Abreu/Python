def gcd(a, b):
    while (b != 0):
        c = a
        a = b
        b = (c % a)
        print(c, a)

        if (b == 0):
            return a
            

print(gcd(18, 35))






    


