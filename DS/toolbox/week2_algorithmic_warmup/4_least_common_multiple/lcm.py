import random 

def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def lcm_fast(a ,b):
    
    upper_limit = a*b + 1#
    lower_num = min(a, b)
    higher_num = max(a, b)
     

    if a == b:
        return a
          
    for j in range(1, upper_limit + 1):
        a_multiple = lower_num*j
        for k in range(1, upper_limit + 1):
            b_multiple = higher_num*k
            # print(a_multiple, b_multiple)
            if b_multiple > a_multiple:
                break
            if a_multiple == b_multiple:
                return a_multiple
    

    
""" if __name__ == '__main__':
  a, b = map(int, input().split())
  print(lcm_fast(a, b)) """

test_num = 100000

for i in range (test_num):
    a = random.randint(1, test_num)
    b = random.randint(1, test_num)
    
    lcm_answer= lcm(a,b)
    lcm_fast_answer = lcm_fast(a, b)
    if lcm_answer != lcm_fast_answer:
        print("input",a  ," ", b, end = ": ")
        print(lcm_answer, " ", lcm_fast_answer) 
