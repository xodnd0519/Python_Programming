# 연산자

# 산술 연산자
a = 10
b = 3
print(a - b, type(a))
print(a + b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**3)

a += 4
print(a)
a -= 10
print(a)

a += 1

# 비교연산자
print(3 == 3.00)
print(3 != 4)
print("apple" < "apble")
print(1 < 2 < 3)
print(1 < 3 < 2)


# short circuit
a = 10
b = 0
print(a / b)
