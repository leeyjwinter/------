num = int(input())
score = []

def prize(x):
    if x.count(x[0]) == 3:
        return 10000 + x[0] * 1000
    elif x.count(x[0]) == 2:
        return 1000 + x[0] * 100
    elif x.count(x[1]) == 2:
        return 1000 + x[1] * 100
    else:
        return max(x) * 100



for i in range(num):

    a = list(map(int,input().split()))
    score.append(prize(a))

print(max(score))







