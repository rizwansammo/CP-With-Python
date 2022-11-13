#Zero Byte Code
#This Program Can be Used in Bruteforce or Dictionary attack
import random
import math
counter = 0
char_list = ['a','e','i','o','u']
#Or
#limit = math.factorial(len(char_list))
while counter <= math.factorial(len(char_list)):
#then
#while counter <= limit:
    random.shuffle(char_list)
    print(''.join(char_list))
    counter+=1
