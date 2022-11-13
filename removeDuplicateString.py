string = " ababacd"
lis = [0] * 26
print(f"Origional string: {string}")
result= ""
for ch in string:
    indx = ord(ch) - ord('a')
    if lis[indx] == 0:
        result=result+ch
        lis[indx] = 1

print(f"Unique characters in string: {result}")
