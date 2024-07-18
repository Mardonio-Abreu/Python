def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_fast(n):

    pisano_period_mod_10 = [0 ,1 ,1 ,2 ,3 ,5 ,8 ,3 ,1 ,4 ,5 ,9 ,4 ,3 ,7 ,0 ,7 ,7 ,4 ,1 ,5 ,6 ,1 ,7 ,8 ,5 ,3 ,8 ,1 ,9 ,0 ,9 ,9 ,8 ,7 ,5 ,2 ,7 ,9 ,6 ,5 ,1 ,6 ,7 ,3 ,0 ,3 ,3 ,6 ,9 ,5 ,4 ,9 ,3 ,2 ,5 ,7 ,2 ,9 ,1, 0 ,1 ,1 ,2 ,3 ,5 ,8 ,3 ,1 ,4 ,5 ,9 ,4 ,3 ,7 ,0 ,7 ,7 ,4 ,1 ,5 ,6 ,1 ,7 ,8 ,5 ,3 ,8 ,1 ,9 ,0 ,9 ,9 ,8 ,7 ,5 ,2 ,7 ,9 ,6 ,5 ,1 ,6 ,7 ,3 ,0 ,3 ,3 ,6 ,9 ,5 ,4 ,9 ,3 ,2 ,5 ,7 ,2 ,9 ,1]

    pisano_period_index = (n % 60) 

    fibo_sum = pisano_period_mod_10[pisano_period_index + 2] - 1

    if fibo_sum == -1:
        fibo_sum = 9

    return fibo_sum
    
        
       
     
#Test code

""" n = 600  

for i in range(n):
    if fibonacci_sum(i) != fibonacci_sum_fast(i):
        print(i, ": ", fibonacci_sum(i), " ", fibonacci_sum_fast(i)) """

 
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n)) 
