num = int(input())
a = list(map(int,input().split()))
b = [0]*num

i = 1
for x in a:
    if j==0:
        b.insert(x, i)
        i+=1
    else:
        b.insert(x+(b[:x+1].count(0)))

# b.insert(5,1)
# print(b)
# print(b[:5].count(0))