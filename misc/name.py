import random

def name():
    
    list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(random.choice(list2) + random.choice(list2) + random.choice(list2) + '-' + random.choice(list1) + random.choice(list1) + random.choice(list1))
    
name()