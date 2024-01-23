def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        #return fibonacci_number(n - 1) + fibonacci_number(n - 2)
        
        previous = 0
        next = 1

        for _ in range(n-1):
            previous, next = next, previous + next

        return next
              

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
