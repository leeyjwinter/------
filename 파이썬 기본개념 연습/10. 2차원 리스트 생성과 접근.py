a=[0]*3
#print(a)

a=[[0]*3 for _ in range(3)]
'''변수가 쓸 일 없을 때 _ 넣어도 됨'''
print(a)

(a[0][1])=1 #a의 0행의 1열
print(a)

a[1][2]=2
print(a)

index=1
for x in a:
    print(index,"번째 수 : ",end='')
    print(x)
    index+=1

for x in a:
    for y in x:
        print(y, end=' ')
    print()