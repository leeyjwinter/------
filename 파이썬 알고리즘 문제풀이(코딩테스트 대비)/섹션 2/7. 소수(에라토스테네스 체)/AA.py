num = int(input())
cnt = 0

def isprime(x):
    if x==2:
        return 1
    else:
        for i in range(2,round(x**(1/2))+1):
            if x%i==0:
                return 0
        return 1


for i in range(2,num+1):
    cnt += isprime(i)



print(cnt)

#에라스토테네스 체
'''import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)'''