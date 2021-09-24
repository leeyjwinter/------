num = int(input())
numlist = list(map(int,input().split()))

def reverse(x):
    x=list(str(x))
    x.reverse()
    i=0

    while x[i]=='0':
        x.pop(i)
    realnum=0
    for i in range(len(x),0,-1):
        realnum = realnum + (10**(i-1))*int(x[len(x)-i])
    return realnum


def isprime(x):
    if x==1:
        return 0
    if x==2:
        return 1
    else:
        for i in range(2,round(x**(1/2))+1):
            if x%i==0:
                return 0
        return 1


for x in numlist:
    if isprime(reverse(x))==1:
        print(reverse(x),end=' ')

#for x in numlist:


