#Zero Byte Code
#This Program Can be Used in Bruteforce or Dictionary attack
import random
import math
counter = 0
char_list = ['a','e','i','o','u']
#limit
while counter <= math.factorial(len(char_list)):
    random.shuffle(char_list)
    print(''.join(char_list))
    counter+=1
