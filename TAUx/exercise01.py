import time

real_password = "2687"

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True



def crack_password():
    dictionaryA = ["0000", "1000", "2000", "3000", "4000", "5000",  "6000", "7000", "8000", "9000"]
    dictionaryB = ["000", "100", "200", "300", "400", "500", "600", "700", "800", "900"]
    dictionaryC = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
    dictionaryD = ["0", "1", "2", "3", "4", "5", "6",  "7", "8", "9"]
          
    for i in dictionaryA:
        start_time = time.time()
        flag = check_password(i)
        end_time = time.time()
        elapsed_time = start_time - end_time
        if (flag):
            return True
        elif (not flag and elapsed_time < -0.2):
            password = i[0]
        
    for i in dictionaryB:
        start_time = time.time()
        flag = check_password(password + i)
        end_time = time.time()
        elapsed_time = start_time - end_time
        if (flag):
            return True
        elif (not flag and elapsed_time < -0.3):
            password = password + i[0]

    for i in dictionaryC:
        start_time = time.time()
        flag = check_password(password + i)
        end_time = time.time()
        elapsed_time = start_time - end_time
        if (flag):
            return True
        elif (not flag and elapsed_time < -0.4):
            password = password + i[0]
 
    for i in dictionaryD:
        flag = check_password(password + i)
        if (flag):
            password = password + i
            break
            
    return password 
        
      
   
print(crack_password())

