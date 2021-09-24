a=[list(map(int, input().split())) for _ in range(7)]

def checker(x):
    for i in range(2):
        if x[i]!=x[4-i]:
            return False
    return True

cnt=0

for i in range(7):
    for j in range(7):
        ch1=[]
        ch2=[]
        for s in range(5):
            try:
                ch1.append(a[i][j+s])
            except IndexError:
                continue
        for k in range(5):
            try:
                ch2.append(a[i + k][j])
            except IndexError:
                continue

        if len(ch1)==5:
            if checker(ch1)==True:
                cnt+=1
        if len(ch2) == 5:
            if checker(ch2)==True:
                cnt+=1

print(cnt)