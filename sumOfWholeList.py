
def calculateSum(l):
    sum=0
    for i in l: #parmeter must be a list
        sum+=i
    return sum


li = []
lenth = int(input("Lenth of the list: "))
while len(li) < lenth:
    l = input("Enter your Item to the List: ")
    li.append(l)
print(calculateSum([1,2,3]))
