# Zero Byte Code
numbers  = input()
lis = numbers.split()

a = int(lis[0])
b = int(lis[1])

def greatesCommonDivisor(a, b):
    if (a == 0):
        return b;
    return greatesCommonDivisor(b%a, a);

if (a>0 and a<(10**12+1) and b>=1 and b<(10**12+1)):
    count = 1
    for i in range(2, greatesCommonDivisor(a, b)+1):
        if a%i==0 and b%i==0:
            count = count+1
    print(count)
