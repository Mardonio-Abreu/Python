def naive_gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
                return current_gcd
            
def gcd(a, b):
    if (a == 0):
        mcd = b
    elif (b == 0):
        mcd = a
    else:
        a = max(a, b)
        b = min(a, b)
    
    while (a % b != 0):
        c = a
        a = b
        b = (c % b)

    return a / b



    


if __name__ == "__main__":
    #a, b = map(int, input().split())
    a, b = 24, 4
    print(naive_gcd(a, b))
    print(gcd(a, b))
