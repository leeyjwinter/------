#2차원 배열 선언하는 법

num = int(input())
a= [list(map(int,input().split())) for _ in range(num)]


'''for i in range(num):
    line = list(map(int, input().split()))
    for j in range(num):
            a[i][j]=line[j]'''

max=0
#행의 합들
for i in range(num):
    sum = 0
    for j in range(num):
        sum+=a[i][j]
    if sum>=max:
        max=sum

#열의 합들
for i in range(num):
    sum = 0
    for j in range(num):
        sum+=a[j][i]
    if sum>=max:
        max=sum

#대각선
sum=0

for i in range(num):
    for j in range(num):
        if j==i:
            sum+=a[j][i]
if sum>=max:
    max=sum

#다른 대각선
sum=0
for i in range(num):
    for j in range(num):
        if j+i==num-1:
            sum+=a[j][i]
if sum>=max:
    max=sum

print(max)