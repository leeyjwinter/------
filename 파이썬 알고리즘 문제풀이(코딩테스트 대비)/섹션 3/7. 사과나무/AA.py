num = int(input())
a=[list(map(int,input().split())) for _ in range(num)]

sums = 0

for i in range(num):
    if i<=(num-1)//2:
        temp=i
    else:
        temp=num-1-i
    first = ((num-1)//2)-temp
    last = ((num-1)//2)+temp+1
    sums+=sum(a[i][first:last])

print(sums)