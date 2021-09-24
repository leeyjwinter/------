'''for i in range(1,11):#1부터 10까지

    print("*",end='')'''


'''for i in range(10): #10번 반복(0부터 9까지)
    print(i)



for i in range(10,0,-1): #(10부터 1까지 1씩 작아짐)
    print(i)'''

'''i=1
while(i<10):
    print(i)
    i=i+1'''

'''i=10
while i>=1:
    print(i)
    i=i-1'''


'''while True:
    print(i)
    i+=1

    if i==10:
        break'''


'''for i in range(1,11):
    if i%2==0:
        continue
    print(i)'''

'''# for else 문도 가능(for문이 정상적으로 돌면 else 나오고 break만나든지 해서 정상적으로 수행 안되면 처리 못함
for i in range(11):
    print(i)
    if i==5:
        break
else:
    print(11)

for i in range(11):
    print(i)
else:
    print(11)'''

a=int(input("수를 입력하시오 : "))


for i in range(1,a+1): #1부터 N까지 홀수 출력
    if i%2==1:
        print(i,end=' ')
print()


sum=0
for i in range(1,a+1):
    sum+=i
print(sum)


for i in range(1,a+1):
    if a%i==0:
        print(i,end=' ')

