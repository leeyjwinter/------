#lower
#upper
#isupper
#islower
#find
#count
#isalpha : 공백이 아니라 알파벳이라면
#ord: ASCII 번호 출력
#chr: 숫자의 ASCII 코드 출력





msg="It is Time"

print(msg.upper()) #대문자화
print(msg)
print(msg.lower()) #소문자화

tmp=msg.upper()
print(tmp.find('T'))  #쳐음으로 발견되는 T의 인덱스 번호
print(msg.find('T')) #대문자와 소문자를 구분함

print(tmp[4])
print(tmp.count('T'))
print(msg[:2]) #인덱스 번호 2번 전까지 나옴
print(msg[3:5]) #인덱스 번호 3~4까지

print(len(msg))

for i in range(len(msg)):
    print(msg[i],end=' ')
print()


for x in msg: #문자 하나하나 접근
    print(x,end= ' ')
print()


for x in msg:
    if x.isupper():
        print(x,end='')
print()

for x in msg:
    if x.islower():
        print(x,end='')
print()


for x in msg:
    if x.isalpha():
        print(x,end='')
print()

tmp ='AZ'
for x in tmp:
    print(ord(x),end=' ')
print()

tmp = 'az'
for x in tmp:
    print(ord(x),end=' ')
print()

tmp = 65
print(chr(tmp))