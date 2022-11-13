def reverseString(string):
    reverseString = ''
    index = len(string)
    while index > 0:
        reverseString += string[ index - 1 ]
        index = index - 1
    return reverseString
string = input("Enter: ")
print(reverseString(string))
