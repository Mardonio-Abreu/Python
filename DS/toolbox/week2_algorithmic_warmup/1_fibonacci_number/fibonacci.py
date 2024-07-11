def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number_fast(n):

    next = 1
    previous = 0

    if n == 0:
        return 0
    else:
    
        for _ in range(n-1):
            previous, next = next, previous + next

        return next

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_fast(input_n))
