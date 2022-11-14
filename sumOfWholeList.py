
def calculateSum(l):
    sum=0
    li = []
    lenth = int(input("Lenth of the list: "))
    while len(li) < lenth:
        l = input("Enter your Item to the List: ")
        li.append(l)
    for i in li: #parmeter must be a list
        sum+=i
    return sum


print(calculateSum(li))
