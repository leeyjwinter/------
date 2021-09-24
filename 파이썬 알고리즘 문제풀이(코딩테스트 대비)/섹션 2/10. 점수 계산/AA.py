num = int(input())
ox=list(map(int,input().split()))

res=0
score=1

if ox[0]==1:
    res+=1

for i in range(1,len(ox)):
    if ox[i]==0:
        score=0
    elif ox[i]==ox[i-1] and ox[i]==1:
        score+=1
    else:
        score=1

    res+=score

print(res)
