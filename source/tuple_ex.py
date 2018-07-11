# tuple_Ex.py

# 튜플
# 시퀀스형, 변경불가 자료형

# 튜플 생성 ()
t = (1, 2, 3)
print(t, type(t))

# ()를 생략해도 튜플로 인식
t = 1, 2, "Python"
print(t, type(t))

# 연결 : +
t2 = t + (3, 4, 5)
print("t2", t2)

# 반복 : *
print(t * 3)

# 인덱싱과 슬라이싱 가능
print(t2[2:5])
print("len:",len(t2))

print("---------")
print("packing & unpacking")
# packing, unpacking
print("t2:", t2)

a, b, c, d, e, f = t2
print("Unpacking:",a,b,c,d,e,f)
'''
# 튜플의 요소보다 변수의 수가 적을 때
a, b = t2 #ValueError
print(a, b)
'''

a, *b = t2
print(a, b)

a,b,*c,d,e = t2
print(a, b, c, d, e)