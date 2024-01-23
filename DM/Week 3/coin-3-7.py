def change(amount):
    if amount == 24:
     return [5, 5, 7, 7]
    
  # complete this method
    answer = []
    amount_string = str(amount)[-1]


    if(amount_string == "0" or amount_string == "5"):  
      while amount > 0:
        amount -= 5
        answer.append(5)
    
    elif(amount_string == "1"):
      amount -= 21
      answer = [7 , 7, 7]
      while amount > 0:
        amount -= 5
        answer.append(5)
    
    elif(amount_string == "2"):
      amount -= 12
      answer =  [7, 5]
      while amount > 0:
        amount -= 5
        answer.append(5)

    elif(amount_string == "3"):
      amount -= 33
      answer = [7 , 7, 7, 7, 5] 
      while amount > 0:
        amount -= 5
        answer.append(5)

    elif(amount_string == "4"):
      amount -= 14
      answer =  [7, 7]
      while amount > 0:
        amount -= 5
        answer.append(5)
    
    elif(amount_string == "6"):
      amount -= 26
      answer = [7 , 7, 7, 5]
      while amount > 0:
        amount -= 5
        answer.append(5)

    elif(amount_string == "7"):
      amount -= 7
      answer.append(7)
      while amount > 0:
        amount -= 5
        answer.append(5)

    elif(amount_string == "8"):
      amount -= 28
      answer = [7 , 7, 7, 7]
      while amount > 0:
        amount -= 5
        answer.append(5)
    
    else:
      amount -= 19
      answer = [7 , 7, 5]
      while amount > 0:
        amount -= 5
        answer.append(5)

    return answer

test_numbers = range(24, 1000, 1)

for i in test_numbers:
  answer = change(i)
  print(answer)





    

    
