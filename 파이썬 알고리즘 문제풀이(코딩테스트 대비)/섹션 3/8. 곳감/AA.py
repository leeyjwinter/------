num = int(input())
a = [list(map(int,input().split())) for _ in range(num)]


times= int(input())
for _ in range(times):
    colnum,vec,val=map(int,input().split())
    if vec==0:
        for _ in range(val):
            k=a[colnum-1][0]
            a[colnum-1].pop(0)
            a[colnum-1].append(k)
    else:
        for _ in range(val):
            k=a[colnum-1][num-1]
            a[colnum-1].pop(num-1)
            a[colnum-1].insert(0,k)

line=num
row=0
sumgot=0
while line!=1:
    sumgot+=sum(a[row][(num-1)//2-(line-1)//2:(num-1)//2+(line-1)//2+1])
    line-=2
    row+=1
while line<=num:
    sumgot+=sum(a[row][(num - 1) // 2 - (line - 1) // 2:(num - 1) // 2 + (line - 1) // 2+1])
    line+=2
    row+=1

print(sumgot)