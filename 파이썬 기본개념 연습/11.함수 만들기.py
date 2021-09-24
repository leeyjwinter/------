
'''def add(a,b):
    c=a+b
    print(c)

add(3,5)
'''



'''
def add(a,b):
    c=a+b
    return c


print(add(3,5))


def two_add(a,b):# c와 달리 두개 이상의 값 return 가능(튜플로 저장함)
    c=a+b
    d=a-b
    return c,d


print(two_add(3,2))

'''

a=[12,13,7,9,19]

def isPrime(a):
        for j in range(2,round(a**0.5)):
            if a%j==0:
                return False
        return True

for x in a:
    if isPrime(x):
        print(x,end=' ')


