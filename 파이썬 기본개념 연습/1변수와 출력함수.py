a = 1
A = 2
print(a, A)

# 값 교환
a, A = A, a
print(a, A)
print(type(a), type(A))

a = 12.12312312334534534534534
print(a)
print(type(a))

a = "student"
print(type(a))

# 출력방식
a, b, c = 1, 2, 3
print(a, b, c)

# sep 출력 사잇값
print(a, b, c, sep=',')
print(a, b, c, sep='')
print(a, b, c, sep='\n')

# end 출력 끝값
print(a, end=' ')
print(b, end=' ')
print(c, end=' ')
