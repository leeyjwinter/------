a,b=map(int,input().split())

sums= []

for i in range(1,a+1):
    for j in range(1,b+1):
        sums.append(i+j)

sums.sort()


setsums=set(sums)

maxcount=0
for x in setsums:
    if sums.count(x)>=maxcount:
        maxcount=sums.count(x)



answer = []
for x in setsums:
    if maxcount==sums.count(x):
        answer.append(x)


for i in answer:
    print(i,end=' ')