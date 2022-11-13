def reverseString(string):
    reverseString = ''
    index = len(string)
    while index > 0:
        reverseString += string[ index - 1 ]
        index = index - 1
    return reverseString
case = 0
case = int(input("How Many Time?: "))
counter = 1
while counter <= case:
    string = input("Enter: ")
    print(reverseString(string))
    counter +=1
