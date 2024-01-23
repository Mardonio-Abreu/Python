import time

#print ("Enter the size")
size = input()

#print ("Enter the numbers")
numbers = input()
stringArray = numbers.split()

numberArray = []

for i in stringArray:
    numberArray.append(int(i))
    

numberArray.sort()
numberArray.reverse()

print(int(numberArray[0])*int(numberArray[1]))

print ()

