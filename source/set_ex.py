#세트
# 순서 없고, 중복 없는 객체의 집합
# {} 정의
# in, not in, len

# 세트 만들기
a = {1, 2, 3}
print(a, type(a))

# 포함 여부의 확인
print(2 in a)
print(3 in a)
print(2 not in a)
print(3 not in a)

# 객체를 추가 : add(x)
a.add(4)
print("add(4):", a)
a.add(4)    # 이미 있는 값에 추가
print("add(4):", a) 

# 객체를 제거해 봅시다 : remove(x), discard(x)
a.remove(4)
# a.remove(4)  # KeyError
print("remove(4):", a)

a.discard(4)
print("discard(4):", a) # discard는 객체가 없어도 통과

# 세트에 여러 개의 값을 추가 : update()
a.update({1, 3, 5, 7, 9})
print("update:", a)

# 집합 연산 : 합집합, 교집합, 차집합
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
mask = {3, 6, 9}

# 합집합
print(even.union(odd) == s1)    #짝수와 홀수 집합의 합집합은 전체 집합
print(even | odd == s1)         #연산자 이용한 합집합 구하기

#교집합
print(odd.intersection(mask))  #홀수집합과 3의 배수 집합의 교집합
print(sorted(odd.intersection(mask)))   #sorted 함수를 쓰면 집합도 정렬 가능
print(odd & mask) # & 연산자를 이용

# 차집합
print(s1.difference(even) == odd)   # 전체 집합에서 짝수 집합을 빼면 차집합은 홀수 집합
print(s1 - even)    # - 연산자를 사용

#모집합과 부분집합
print(s1.issuperset(even))  #s1은 even의 모집합인가?
print(even.issubset(s1))    #even은 s1의 부분집합인가?

print({10, 11, 12}.issubset(s1))    # {10, 11, 12}는 s1의 부분집합인가?