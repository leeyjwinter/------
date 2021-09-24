num = int(input())
numlist = list(input().split())
sumofnum = []


def digit_sum(x):
    sum=0
    x=str(x)
    a= int(x)
    for i in range(len(x),0,-1):
        mok = a//10**(i-1)
        sum+=mok
        a = a-mok*((10)**(i-1))
    return sum


for x in numlist:
    sumofnum.append(digit_sum(x))

print(numlist[sumofnum.index(max(sumofnum))])


'''for i in str(x):
    sum+=int(i) 하면 자릿수별 합 바로 구하기 가능'''