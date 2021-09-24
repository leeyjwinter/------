num = int(input())
for i in range(num):
    a=input()
    a=a.lower()
    b=''.join(reversed(a))

    if a==b:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')

#print(a[::-1])하는 것도 가능 - 거꾸로 출력해줌
