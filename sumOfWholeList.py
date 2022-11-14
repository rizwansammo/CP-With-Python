
def calculateSum():
    sum=0
    li = []
    lenth = int(input("Lenth of the list: "))
    while len(li) < lenth:
        l = int(input("Enter your Item to the List: "))
        li.append(l)
    for i in li:
        sum+=i
    print(f"Sum is {sum}")

calculateSum()
