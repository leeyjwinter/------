num = int(input())
a=[(list(map(int,input().split()))) for _ in range(num)]
cnt=0

for i in range(num):
    for j in range(num):
        if i-1>=0:
            up=a[i -1][j]
        else:
            up=0

        if i+1==num:
            down=0
        else:
            down=a[i+1][j]

        if j-1>=0:
            left=a[i][j-1]
        else:
            left=0

        if j+1==num:
            right=0
        else:
            right = a[i][j + 1]


        if a[i][j]>up and a[i][j]>down and a[i][j]>left and a[i][j]>right:
            #print(f'a[{i}][{j}]={a[i][j]}')
            cnt+=1

print(cnt)

