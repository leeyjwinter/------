import heapq as hq

a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n==0:
        if len(a)==0:
            break
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)
