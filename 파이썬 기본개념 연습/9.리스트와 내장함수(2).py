#enumerate(a) a의 인덱스와 그에 따른 리스트 값을 튜플로 저장

# 튜플은 리스트와 같은 함수를 이용할 수 있으나 값을 바꿀 수는 없음!!

# all(조건1 조건2): 조건이 모두 참이면 true 반환
# any(조건1 조건2): 조건이 하나라도 참이면 true 반환



a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x,end=' ')
print()


for x in a:
    if x%2==1:
        print(x,end=' ')
print()


for x in enumerate(a):
    print(x, end= ' ')
print()

b=(1,2,3,4,5)
print(b[0])

for index,value in enumerate(a):
    print(index,value,sep=' ', end='   ')
print()

if all(60>x for x in a):
    print("All True")

print(all(60>x for x in a))

if any(15>x for x in a):
    print("Least one is true")

if any(1<2 and 2>1):
    print("Least one is true")


