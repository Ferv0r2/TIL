# 변수 초기화 방법
a = 1
b = 1.2
c = 'a'
d = 'abc'
e = True
print(type(a), type(b), type(c), type(d), type(e))
print(id(a))
a = c = 1.1
print(a, type(a), id(a))

# 연산자
a = 1
b = 2
hap = a+b  # 합
min = a-b  # 빼기
mul = a*b  # 곱
div = a/b  # 나누기
share = a//b  # 몫
rest = a % b  # 나머지
square = b ** b  # 제곱
print(hap, min, mul, div)
print(share, rest, square)

a += 1
print(a)
a -= 1
print(a)
a == 1
print(a)
a != 1
print(a)

print(a >> 1, a << 1)

# 조건문 ( 선택문 )
a = 1
b = 2
c = 3
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(c)
if a > b:
    if a > c:
        print(a)
    else:
        print(b)
    print(c)

# 반복문 while
sum = 0
i = 1
while True:
    if sum == 10:
        break
    sum += i

while sum <= 0:
    sum -= i

# 반복문 for
for i in range(10):
    print(i)

for i in range(10, 1, -1):
    print(i)

# 클래스 정의 및 객체 생성 방법


class Human:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def print(self):
        print(f'이름은 {self.name}, 성별은 {self.sex}, 나이는 {self.age}입니다')


man = Human('wontae', 'male', '24')
man.print()
