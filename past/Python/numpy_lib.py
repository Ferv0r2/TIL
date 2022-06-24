import numpy as np

# 배열 생성 방법
a = []
b = [1, 2]
c = [1, 'a', 2.3]
print(a, b, c)

# 인덱싱 슬라이싱
animal = 'dog'
print(animal[1])
print(animal[-2])
print(animal[0:1])
print(animal[:])
print(animal[1:])
print(animal[:2])

# 넘파이 제공 함수
n = np.array([1, 2, 3])
print(n)
print(n.shape)  # 객체의 형태(shape)
print(n.ndim)  # 객체의 차원
print(n.dtype)  # 객체의 내부 자료형
print(n.itemsize)  # 메모리 크기
n.size  # 전체 크기

n = n + 100
print(n)

# 필터링
filter_list = []
for x in n:
    if x % 2 == 0:
        filter_list.append(True)
    else:
        filter_list.append(False)

newarr = n[filter_list]
print(filter_list)
print(newarr)
