#a.append(6) 6을 뒤에 추가
#a.insert(3,7) 3번 인덱스에 7 추가
# a.pop() 맨 뒷 문자 제거
# a.pop(3) 3번째 문자 제거
#a.remove(4) 4라는 값을 제거
# a.index(5) 5라는 값의 인덱스 번호
# r.shuffle(a) 리스트 값들 셔플
# a.sort() 오름차순 정렬, a.sort(reverse=True) 내림차순 정렬
# a.clear() 리스트 a 비우기
# a.index('a') a문자 인덱스 찾기
# a.count("a") a문자 몇개 있는지 찾기
import random as r
a=[]

b=list()
print(b)

a=[1,2,3]
print(a)


b=list(range(1,11))
print(b)

c=a+b
print(c)

a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)

a.pop(3)
print(a)

a.remove(1)
print(a)

print(a.index(2))


a=list(range(1,11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(min(7,2,3))

r.shuffle(a)
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.clear()
print(a)