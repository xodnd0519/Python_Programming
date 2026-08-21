# 파이썬 자료형
# 1. 기본 자료형 : 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합

# 숫자형
# 정수형(int)
a = 10
print(a, type(a))

# 2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))
print(ord("A"), chr(65))

# 정수 데이터 범위
x = 10**100
print(x, type(a))

# 실수형 (float)
b = 3.14
print(b, type(b))
a = float(22 / 7)
print(a, type(a))

import sys

print(sys.float_info)
print(-sys.float_info.max)

a = 1.7e308
b = 1.8e308
print(a, b, sep="       ")

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.5:.20f}")

# 형변환
print(float(100))
print(int(3.14))
print(float("3.14"))
print(int("3"))
print(ord("A"))
