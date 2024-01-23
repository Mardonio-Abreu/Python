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
        min_number = min(a, b)
        max_number = max(a,b)
    
        

    return mcd

    


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(naive_gcd(a, b))
