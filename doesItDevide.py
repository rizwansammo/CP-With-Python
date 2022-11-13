testCase = int(input())
arr=[]
for i in range(1,testCase+1):
    arr.append(int(input()))

for n in arr:
    if n>=1 and n<=(10**9):
        product = 1
        sum = 0
        for i in range(1, n+1):
            product = product*i
            sum = sum+i
        if product%sum==0:
            print("Y")
        else:
            print("N")
